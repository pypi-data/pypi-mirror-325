import copy
import multiprocessing
import threading
import timeit
from multiprocessing import Queue
from threading import Thread

import numpy as np
import shapely

from trajallocpy import ACBBA, CBBA, Agent, CoverageProblem, Utility


class Runner:
    def __init__(self, coverage_problem: CoverageProblem.CoverageProblem, agents: list[Agent.config], enable_plotting=False):
        # Task definition
        self.coverage_problem = coverage_problem
        self.robot_list = {}

        for agent in agents:
            self.robot_list[agent.id] = CBBA.agent(
                id=agent.id,
                state=shapely.Point(agent.position),
                environment=copy.deepcopy(self.coverage_problem.environment),
                tasks=np.array(self.coverage_problem.getTasks()),
                capacity=agent.capacity,
                number_of_agents=len(agents),
                point_estimation=False,
            )
        self.communication_graph = np.ones((len(agents), len(agents)))
        self.plot = enable_plotting

        # Results
        self.routes = {}
        self.transport = {}
        self.tasks = {}

    def evaluateSolution(self, show=True):
        path_lengths = {}
        task_length = {}
        path_costs = {}
        route_list = {}
        rewards = {}
        for r in self.robot_list.values():
            r: CBBA.agent
            path_lengths[r.id] = Agent.getTotalPathLength(r.state, r.getPathTasks(), r.environment)
            task_length[r.id] = Agent.getTotalTaskLength(r.getPathTasks())
            path_costs[r.id] = Agent.getTotalTravelCost(r.state, r.getPathTasks(), r.environment)
            rewards[r.id] = Agent.calculatePathReward(r.state, r.getPathTasks(), r.environment, r.capacity, r.Lambda)

            route = [r.state]
            for task in r.getPathTasks():
                route.extend(list(task.trajectory.coords))
            route.append(r.state)
            route_list[r.id] = route
        print("Results")
        print("Execution time: ", self.end_time - self.start_time)
        print("Iterations: ", self.iterations)
        print("Path lengths: ", path_lengths)
        print("Task lengths: ", task_length)
        print("Path costs: ", path_costs)
        print("Rewards: ", rewards)
        # print("Routes: ", route_list)
        max_path_cost = max(path_costs.values())
        print("Max path cost: ", max_path_cost)
        print("Sum of path lengths: ", sum(path_lengths.values()))
        print("Sum of task lengths: ", sum(task_length.values()))
        print("Sum of path costs: ", sum(path_costs))
        print("Sum of rewards: ", sum(rewards.values()))
        return (
            self.end_time - self.start_time,
            self.iterations,
            path_lengths,
            task_length,
            path_costs,
            rewards,
            route_list,
            max_path_cost,
        )

    def add_tasks(self, tasks):
        # TODO make sure that the tasks are within the search area

        # TODO make sure that the tasks not already in the list
        for robot in self.robot_list:
            robot.add_tasks(tasks)

    def solve(self, profiling_enabled=False, debug=False):
        if profiling_enabled:
            print("Profiling enabled!")
            import cProfile
            import io
            import pstats
            from pstats import SortKey

            pr = cProfile.Profile()
            pr.enable()
        t = 0  # Iteration number

        if self.plot:
            plotter = Utility.Plotter(self.robot_list.values(), self.communication_graph)
            # Plot the search area and restricted area
            plotter.plotPolygon(self.coverage_problem.getSearchArea(), color=(0, 0, 0, 0.5))
            if self.coverage_problem.getRestrictedAreas() is not None:
                plotter.plotMultiPolygon(self.coverage_problem.getRestrictedAreas(), color=(0, 0, 0, 0.2), fill=True)
        self.start_time = timeit.default_timer()

        result_queue = multiprocessing.Queue()
        # result_queue.cancel_join_thread()
        use_threads = True
        while True:
            print("Iteration {}".format(t + 1))
            # Phase 1: Auction Process

            # Create a list to store the threads
            processes: list[multiprocessing.Process] = []
            # Start multiple threads
            if use_threads:
                for robot in self.robot_list.values():
                    # robot.build_bundle(result_queue)
                    process = multiprocessing.Process(target=robot.build_bundle, args=(result_queue,))
                    process.start()
                    processes.append(process)

                # Wait for all processes to finish
                for process in processes:
                    process.join()

                # Extract results from the queue
                while not result_queue.empty():
                    result = result_queue.get()
                    self.robot_list[result.id].update_bundle_result(result)
            else:  # Single thread
                for robot in self.robot_list.values():
                    robot.build_bundle()
            if debug:
                print("Bundle")
                for robot in self.robot_list.values():
                    print(robot.bundle)
                print("Path")
                for robot in self.robot_list.values():
                    print(robot.path)
            previous_bundle = {robot_id: robot.bundle.copy() for robot_id, robot in self.robot_list.items()}

            # Do not communicate if there are no agents to communicate with
            if len(self.robot_list) <= 1:
                break

            # Communication stage
            message_pool = [robot.send_message() for robot in self.robot_list.values()]
            conflicts = 0
            # Phase 2: Consensus Process
            if isinstance(self.robot_list[0], ACBBA.agent):  # ACBBA
                messages = 0
                for robot in self.robot_list.values():
                    robot: ACBBA.Agent
                    # Update local information and decision
                    conflicts += len(robot.update_task(robot.Y))

                if messages == 0:
                    break
            else:  # CBBA
                for robot_id, robot in self.robot_list.items():
                    robot: CBBA.agent
                    # Recieve winning bidlist from neighbors
                    g = self.communication_graph[robot_id]

                    (connected,) = np.where(g == 1)
                    connected = list(connected)
                    connected.remove(robot_id)
                    print(robot.winning_bids)
                    conflicts += robot.update_task({neighbor_id: message_pool[neighbor_id] for neighbor_id in connected})
                if debug:
                    print("Conflicts:", conflicts)

            # Check for convergence
            bundle_diff = {robot_id: set(previous_bundle[robot_id]) - set(robot.bundle) for robot_id, robot in self.robot_list.items()}
            if debug:
                print("Bundle Difference:", bundle_diff)
            if all(len(s) == 0 for s in bundle_diff.values()):
                break

            if debug:
                # Plot
                if self.plot:
                    plotter.setTitle("Time Step:{}".format(t))
                    plotter.plotAgents(self.robot_list.values())
                    plotter.pause(0.1)
                    # plotter.save("iteration{}.png".format(t))

                print("Bundle")
                for robot in self.robot_list.values():
                    print(robot.bundle)
                print("Path")
                for robot in self.robot_list.values():
                    print(robot.path)

            t += 1

        self.iterations = t

        if profiling_enabled:
            print("Profiling finished:")
            s = io.StringIO()
            sortby = SortKey.CUMULATIVE
            ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
            ps.print_stats(100)
            pr.disable()

        self.end_time = timeit.default_timer()

        # Save the results in the object
        for robot in self.robot_list.values():
            self.routes[robot.id], self.transport[robot.id], self.tasks[robot.id] = Agent.getTravelPath(
                robot.state, robot.getPathTasks(), robot.environment
            )
        # Print the agent bundles
        for robot_id, robot in self.robot_list.items():
            print(f"Agent {robot_id} bundle: {robot.bundle}")
            print(f"Agent {robot_id} path: {robot.path}")

        if self.plot:
            plotter.plotAgents(self.robot_list.values())
        if self.plot:
            plotter.show()
