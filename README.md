SesnaQuake
SesnaQuake is a prototype Earthquake Early Warning (EEW) monitoring tool that listens to various real-time EEW data sources using WebSocket connections. It provides detailed earthquake alerts for multiple regions, including Japan, China, and other parts of Asia.

This is an early-stage project and is not yet production-ready. Feedback and contributions are highly encouraged to improve the system.

Features
Multi-Region Support: Receives EEW alerts from:

Japan Meteorological Agency (JMA EEW)
China Earthquake Networks Center (CENC EEW)
China Earthquake Administration (CWA EEW)
Sichuan EEW (SC EEW)
Fujian EEW (FJ EEW)
Real-Time Alerts: Displays detailed information such as magnitude, depth, location, maximum intensity, and more.

Multi-Threaded WebSocket Connections: Simultaneously monitors multiple EEW data sources for fast and reliable updates.

Custom Sound Notifications: (Planned Feature) Integration with the playsound library for audible warnings.

Prerequisites
Python 3.7+
Required Python packages:
bash
Copy
Edit
pip install websocket-client playsound
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/SesnaQuake.git
cd SesnaQuake
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Edit the WebSocket URLs if necessary (found in the ws_urls dictionary in the main script).

Usage
Run the script directly using Python:

bash
Copy
Edit
python sesnaquake.py
The tool will:

Establish WebSocket connections to multiple EEW services.
Display real-time earthquake alerts for the monitored regions.
Example Output
When an earthquake alert is received, the script will display information like:

yaml
Copy
Edit
Earthquake Alert! (JAPAN EEW)
Title: Major Earthquake
Location: Tokyo Bay
Magnitude: 6.5, Depth: 40 km
Max Intensity: 5+
Maximum earthquake intensity: 5+
Origin time: 2025-01-16 23:45:00
Warning area arrival: Immediate
Type: Preliminary
Warning Areas: [Tokyo, Yokohama, Chiba]
If no alerts are issued, the tool will print No EEW issued periodically.

Limitations
Prototype Status: SesnaQuake is still in development and may contain bugs or incomplete features.
Reliability: Not yet optimized for high reliability or scalability.
Audible Alerts: Sound notifications are not fully implemented in this version.
Data Sources: Relies on third-party WebSocket services that may change or become unavailable.
Roadmap
 Improve alert handling and display.
 Add customizable sound notifications.
 Enhance error handling and reconnection logic.
 Provide better configuration options for users.
 Expand to support more data sources.
Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Feel free to submit issues for bugs or feature requests.

License
SesnaQuake is licensed under the MIT License.

Disclaimer
SesnaQuake is a prototype and is not intended to replace official government warnings or emergency alerts. Always follow local guidelines and official instructions during seismic events. Use this tool at your own risk.
