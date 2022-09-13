So this isn't a whole lot, it's basically just a script that will read in the data output by an AQI sensor that's been sold on Banggood:

https://usa.banggood.com/PM1_0-PM2_5-PM10-Meaturing-Module-Air-Quality-Dust-Sensor-Tester-Support-Export-Data-Monitoring-Home-Office-Car-Tools-p-1615550.html

The device has a PMS5003 attached to an MCU and it will, if you poke the USB port correctly, dump some of the PMS5003 data out the serial port.  This is obviously
not an exhausitve list of the data that the PMS5003 provides, but it does work.

# Noting command structure

The commands are not super well documented and in case they disappear from the Banggood listing I'm noting them here:

{"fun":"05","flag":"1"} - Starts realtime stream data

{"fun":"05","flag":"0"} - Stops realtime stream data

{"fun":"05","flag":"0"}}{"fun":"80"} - Stop and enter config mode
Response: {res:80,SendInteralTime:000020,StoreInteralTime:000000,WritePoint:000000,ReadPoint:000000,SendInteralFlag:000000,}

{"fun":"01","sendtime":"020"}}{"res":"1"}{"fun":"05","flag":"0"}}{"fun":"05","flag":"1"} - Set realtime interval to 20 seconds, start stream data

{"fun":"03","clock":"20-09-14 18:53:56"}} - Set time to example

# License
MIT

Copyright 2022 John 'Warthog9' Hawley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
