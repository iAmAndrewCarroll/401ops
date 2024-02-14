import ipaddress
import sys
import os
import unittest  # Add this line to import unittest module
from unittest.mock import patch, MagicMock, call  # Add this line to import patch and MagicMock

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

# Now perform the relative import
from ops26_2_core import scan_port, export_results, generate_ip_range, icmp_ping_sweep, scan_ip_and_ports

class TestOps26Core(unittest.TestCase):

    def test_scan_port_open(self):
        # Mocking the sr1 function to simulate an open port response
        with patch("ops26_2_core.sr1") as mock_sr1:
            mock_resp = MagicMock()
            mock_resp.haslayer.return_value = True
            mock_resp.getlayer.return_value.flags = 0x12  # SYN-ACK
            mock_sr1.return_value = mock_resp

            result = scan_port("192.168.0.215", 80)
            self.assertEqual(result, (80, "Open"))

    def test_scan_port_closed(self):
        # Mocking the sr1 function to simulate a closed port response
        with patch("ops26_2_core.sr1") as mock_sr1:
            mock_resp = MagicMock()
            mock_resp.haslayer.return_value = True
            mock_resp.getlayer.return_value.flags = 0x14  # RST-ACK
            mock_sr1.return_value = mock_resp

            result = scan_port("192.168.0.215", 80)
            self.assertEqual(result, (80, "Closed"))

    def test_scan_port_filtered(self):
        # Mocking the sr1 function to simulate no response (filtered port)
        with patch("ops26_2_core.sr1") as mock_sr1:
            mock_sr1.return_value = None

            result = scan_port("192.168.0.215", 80)
            self.assertEqual(result, (80, "Filtered"))

    def test_export_results_csv(self):
        # Mocking pandas DataFrame.to_csv method
        with patch("pandas.DataFrame.to_csv") as mock_to_csv:
            export_results([(80, "Open"), (443, "Closed")], "scan_results")
            mock_to_csv.assert_called_once_with("scan_results.csv", index=False)

    def test_generate_ip_range_valid_cidr(self):
        result = generate_ip_range("192.168.0.0/24")
        network = ipaddress.ip_network("192.168.0.0/24", strict=False)
        expected = [str(ip) for ip in network.hosts()]
        self.assertEqual(result, expected)



    def test_generate_ip_range_invalid_cidr(self):
        result = generate_ip_range("invalid_cidr")
        self.assertEqual(result, [])  # Empty list for invalid CIDR

    def test_icmp_ping_sweep_all_responding(self):
        # Mocking sr1 function to simulate all IPs responding
        with patch("ops26_2_core.sr1") as mock_sr1:
            mock_sr1.return_value = MagicMock()

            ip_list = ["192.168.0.215", "192.168.0.216"]
            with patch("builtins.print") as mock_print:
                icmp_ping_sweep(ip_list)
                mock_print.assert_called_with("\nTotal online hosts: 2")

    def test_icmp_ping_sweep_some_blocked(self):
        # Mocking sr1 function to simulate some IPs blocked
        with patch("ops26_2_core.sr1") as mock_sr1:
            # Mock a response indicating ICMP traffic is blocked for the first IP
            mock_resp_blocked = MagicMock()
            mock_resp_blocked.haslayer.return_value = True
            mock_resp_blocked.getlayer.return_value.type = 3  # ICMP Destination Unreachable
            mock_resp_blocked.getlayer.return_value.code = 1  # Code indicating communication administratively prohibited
            # Mock a response indicating ICMP traffic is not blocked for the second IP
            mock_resp_not_blocked = MagicMock()
            mock_resp_not_blocked.haslayer.return_value = False  # Simulating no response

            # Set up mock_sr1 to return the appropriate responses for each IP
            mock_sr1.side_effect = [mock_resp_blocked, mock_resp_not_blocked]

            # Define the list of IP addresses to test
            ip_list = ["192.168.0.215", "192.168.0.216"]

            # Patch the print function for testing
            with patch("builtins.print") as mock_print:
                # Call the function under test
                icmp_ping_sweep(ip_list)

                # Check the calls to print function
                calls = [call_args[0] for call_args, _ in mock_print.call_args_list]
                print("Printed messages during test:", calls)
                # Adjust the assertions to match the expected behavior
                mock_print.assert_any_call("192.168.0.215 is actively blocking ICMP traffic.")
                mock_print.assert_any_call("192.168.0.216 is responding.")
                mock_print.assert_any_call("\nTotal online hosts: 1")

    def test_scan_ip_and_ports_interrupted(self):
        # Mocking scan_port to simulate an interrupted scan
        with patch("ops26_2_core.scan_port") as mock_scan_port:
            mock_scan_port.side_effect = [(80, "Open"), (443, "Interrupted")]

            with patch("builtins.print") as mock_print:
                scan_ip_and_ports("192.168.0.215")
                mock_print.assert_called_with("Scan interrupted by user.")

if __name__ == "__main__":
    unittest.main()
