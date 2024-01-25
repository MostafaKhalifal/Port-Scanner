# Port Scanner Project
# Introduction

This is a simple Python port scanner designed to help you identify open ports on a target host. The script uses multi-threading to perform concurrent port scans, making it faster and more efficient.
# Features

    Multi-threading: Utilizes the concurrent.futures.ThreadPoolExecutor to concurrently scan multiple ports.
    Command-Line Interface: Takes command-line arguments for specifying the target host, start and end ports, and the number of threads for concurrent scanning.
    Timeout Handling: Sets a timeout of 1 second for each socket connection, making the scanning process more responsive.

# Getting Started

To use the port scanner, follow these steps:

    Clone the repository:

    bash

git clone https://github.com/your-username/port-scanner.git

Navigate to the project directory:

bash

cd port-scanner

Run the script with the desired parameters:

bash

    python port_scanner.py <target_host> <start_port> <end_port> [-t/--threads <num_threads>]

# Usage

bash

python port_scanner.py <target_host> <start_port> <end_port> [-t/--threads <num_threads>]

    <target_host>: The target host to scan.
    <start_port>: The starting port of the scan range.
    <end_port>: The ending port of the scan range.
    -t/--threads <num_threads>: (Optional) Number of threads for concurrent scanning. Default is 10.
