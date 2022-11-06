# What is CANbus

The Controller Area Network, is a communication its a message-based protocol(a set of rules for the exchange of data between devices)

PDO: Process Data Object - Inputs and outputs. Values of type rotational speed, voltage,Vector CANeds 3.6 frequency electric current.

SDO: Service Data Object - Configuration settings, possibly node ID, baud rate, offset, gain.

COB-ID: Communication object identifier

CAN ID: CAN Identifier. This is the 11-bit CAN message identifier which is at the beginning of every CAN message on the bus.

EDS: Electronic Data Sheet. This is an INI style or XML style formatted file.

DCF: Device Configuration File. This is a modified EDS file with settings for node ID and baud rate.

## In depth 
SDO:  reads/writes to one dedicated CANopen object address, the SDO has always the initiative sending messages.
Each frame sent by SDO client is confirmed by the SDO server with a CAN frame.
SDO services are intender to configure or diagnose a CANopen device.
SDO services increase the busload.

PDO: Process Data Object(PDO) used to transmit time-critical data like measured values or commands.
the PDO service is not confirmed(it does not talk back) it is a pub/sub type service.
PDO's are mapped to a single CAN data frame using a CAN-ID determined by the COB-ID parameter in the object dictionary.
transmision type is also set here reception/transmision rx/tx
