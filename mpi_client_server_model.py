from mpi4py import MPI
import random
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ROUNDS = 3

# Server
if rank == 0:
    print("\n[SERVER] Started")

    for r in range(ROUNDS):
        print(f"\n[SERVER] Round {r+1}")

        data_list = []

        for i in range(1, size):
            data = comm.recv(source=i)
            print(f"Received {data} from Client {i}")
            data_list.append(data)

        total = sum(data_list)
        avg = total / len(data_list)

        print(f"Total = {total}, Average = {avg}")

        for i in range(1, size):
            comm.send((total, avg), dest=i)

# Clients
else:
    for r in range(ROUNDS):
        time.sleep(1)

        data = random.randint(1, 100)
        print(f"Client {rank} generated: {data}")

        comm.send(data, dest=0)

        total, avg = comm.recv(source=0)
        print(f"Client {rank} received -> Total: {total}, Avg: {avg}")
