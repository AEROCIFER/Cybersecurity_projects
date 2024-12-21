from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Define the file to store the captured packet data
log_file = "network_log.txt"

def packet_callback(packet):
    try:
        # Open the log file in append mode
        with open(log_file, "a") as file:
            # Check if the packet has an IP layer
            if IP in packet:
                src_ip = packet[IP].src
                dst_ip = packet[IP].dst
                protocol = packet[IP].proto

                # Identify the transport layer protocol
                if protocol == 6:  # TCP
                    proto_name = "TCP"
                elif protocol == 17:  # UDP
                    proto_name = "UDP"
                else:
                    proto_name = "Other"

                # Log basic packet information
                log_entry = f"Protocol: {proto_name}, Source: {src_ip}, Destination: {dst_ip}\n"
                print(log_entry, end="")
                file.write(log_entry)

                # Extract and log payload data
                try:
                    payload = bytes(packet[TCP].payload) if protocol == 6 else bytes(packet[UDP].payload)
                    if payload:
                        payload_data = payload.decode("utf-8", errors="replace")  # Use UTF-8 with error handling
                        payload_log = f"Payload Data: {payload_data}\n"
                        print(payload_log)
                        file.write(payload_log)
                except Exception as e:
                    error_log = f"Payload could not be processed: {e}\n"
                    print(error_log)
                    file.write(error_log)      

                # Add a separator for clarity
                file.write("-" * 50 + "\n")

    except Exception as e:
        print(f"Error writing to file: {e}")

# Start sniffing packets
print("Starting packet capture. Packet details will be logged to 'network_log.txt'. Press Ctrl+C to stop.")
sniff(prn=packet_callback, store=False)
