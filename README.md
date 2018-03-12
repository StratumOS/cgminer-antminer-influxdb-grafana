# cgminer-antminer-influxdb-grafana
Script for monitoring cgminer based cryptocurrency miners in Grafana dashboard

Usage:
cgminer-api-pull-data.py [command] [ip] [port]
eg. cgminer-api-pull-data.py summary 192.168.1.10 4028

Output (from Antminer S7):
{'SUMMARY': [{'Utility': 5.85, 'Device Rejected%': 0.6103, 'Remote Failures': 0, 'Difficulty Stale': 0.0, 'Get Failures': 0, 'Rejected': 102, 'Difficulty Accepted': 219627520.0, 'Getworks': 5126, 'Found Blocks': 0, 'Local Work': 445105685, 'Work Utility': 51867.62, 'Hardware Errors': 3, 'Pool Rejected%': 0.6154, 'Total MH': 957072215876.0, 'Last getwork': 1520855087, 'GHS 5s': 3712.97, 'GHS av': 3712.83, 'Discarded': 103007, 'Stale': 0, 'Pool Stale%': 0.0, 'Difficulty Rejected': 1359872.0, 'Network Blocks': 442, 'Best Share': 0, 'Accepted': 25137, 'Elapsed': 257774, 'Device Hardware%': 0.0}], 'id': 1, 'STATUS': [{'Code': 11, 'When': 1520855087, 'Description': 'cgminer 4.8.0', 'Msg': 'Summary', 'STATUS': 'S'}]}

