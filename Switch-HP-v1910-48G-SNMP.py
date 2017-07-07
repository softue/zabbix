#!/usr/bin/env python
# *-* coding:utf-8 *-*

"""

	Zabbix Template Switch HP v1910 48G SNMP
	Copyright (C) 2017 Rômulo Mendes Figueiredo	

	This script expands the original 24 ports template to 48 ports and made compatible with Zabbix 2.0.6+
	Original template published by Павел Яковлев on <https://share.zabbix.com/network_devices/cat-hp/zabbix-2-2-hp-v1910-snmp-template>
	
	How to use:
	-----------
	$ chmod +x ./Switch-HP-v1910-48G-SNMP.py
	$ ./Switch-HP-v1910-48G-SNMP.py > Switch-HP-v1910-48G-SNMP.xml

"""

xmlHead="""<?xml version="1.0" encoding="UTF-8"?>
<zabbix_export>
    <version>2.0</version>
    <date>2017-06-21T14:09:55Z</date>
    <groups>
        <group>
            <name>Templates</name>
        </group>
    </groups>"""
print(xmlHead)


templatesIni="""    <templates>
        <template>
            <template>Template SNMP HP v1910-48G</template>
            <name>Template SNMP HP v1910-48G</name>
            <groups>
                <group>
                    <name>Templates</name>
                </group>
            </groups>
            <applications>
                <application>
                    <name>Bytes Rx</name>
                </application>
                <application>
                    <name>Bytes Tx</name>
                </application>
                <application>
                    <name>CRC Errors Rx</name>
                </application>
                <application>
                    <name>CRC Errors Tx</name>
                </application>
                <application>
                    <name>General</name>
                </application>
                <application>
                    <name>Oper Status</name>
                </application>
            </applications>
            <items>"""
print(templatesIni)



BytesRx="""                <item>
                    <name>Bytes Rx port {p}</name>
                    <type>4</type>
                    <snmp_community>{{$SNMP_COMMUNITY}}</snmp_community>
                    <multiplier>1</multiplier>
                    <snmp_oid>1.3.6.1.2.1.2.2.1.10.{p}</snmp_oid>
                    <key>ifInOctets.{p}</key>
                    <delay>120</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units>bps</units>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>8</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{{$SNMP_PORT}}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Bytes Rx</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>"""
for port in range(1,49):
	print(BytesRx.format(p=port))


BytesTx="""                <item>
                    <name>Bytes Tx port {p}</name>
                    <type>4</type>
                    <snmp_community>{{$SNMP_COMMUNITY}}</snmp_community>
                    <multiplier>1</multiplier>
                    <snmp_oid>1.3.6.1.2.1.2.2.1.16.{p}</snmp_oid>
                    <key>ifOutOctets.{p}</key>
                    <delay>120</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units>bps</units>
                    <delta>1</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>8</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{{$SNMP_PORT}}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Bytes Tx</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>"""
for port in range(1,49):
	print(BytesTx.format(p=port))


InErrors="""                <item>
                    <name>InErrorsFa0/{p}</name>
                    <type>4</type>
                    <snmp_community>{{$SNMP_COMMUNITY}}</snmp_community>
                    <multiplier>0</multiplier>
                    <snmp_oid>.1.3.6.1.2.1.2.2.1.14.{p}</snmp_oid>
                    <key>ifInErrors.{p}</key>
                    <delay>120</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{{$SNMP_PORT}}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>CRC Errors Rx</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>"""
for port in range(1,49):
	print(InErrors.format(p=port))


print("""                <item>
                    <name>Model</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <multiplier>0</multiplier>
                    <snmp_oid>.1.3.6.1.2.1.1.1.0</snmp_oid>
                    <key>.1.3.6.1.2.1.1.1.0</key>
                    <delay>3600</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>4</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{$SNMP_PORT}</port>
                    <description/>
                    <inventory_link>29</inventory_link>
                    <applications>
                        <application>
                            <name>General</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>""")



OutErrors="""                <item>
                    <name>OutErrorsFa0/{p}</name>
                    <type>4</type>
                    <snmp_community>{{$SNMP_COMMUNITY}}</snmp_community>
                    <multiplier>0</multiplier>
                    <snmp_oid>.1.3.6.1.2.1.2.2.1.20.{p}</snmp_oid>
                    <key>ifOutErrors.{p}</key>
                    <delay>120</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{{$SNMP_PORT}}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>CRC Errors Tx</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>"""
for port in range(1,49):
	print(OutErrors.format(p=port))


Status="""                <item>
                    <name>Status port {p}</name>
                    <type>4</type>
                    <snmp_community>{{$SNMP_COMMUNITY}}</snmp_community>
                    <multiplier>0</multiplier>
                    <snmp_oid>1.3.6.1.2.1.2.2.1.8.{p}</snmp_oid>
                    <key>ifOperStatus.{p}</key>
                    <delay>120</delay>
                    <history>7</history>
                    <trends>365</trends>
                    <status>1</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units/>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>1</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{{$SNMP_PORT}}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>Oper Status</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>"""
for port in range(1,49):
	print(Status.format(p=port))


print("""                <item>
                    <name>Uptime</name>
                    <type>4</type>
                    <snmp_community>{$SNMP_COMMUNITY}</snmp_community>
                    <multiplier>1</multiplier>
                    <snmp_oid>.1.3.6.1.2.1.1.3.0</snmp_oid>
                    <key>Uptime</key>
                    <delay>60</delay>
                    <history>90</history>
                    <trends>365</trends>
                    <status>0</status>
                    <value_type>3</value_type>
                    <allowed_hosts/>
                    <units>s</units>
                    <delta>0</delta>
                    <snmpv3_contextname/>
                    <snmpv3_securityname/>
                    <snmpv3_securitylevel>0</snmpv3_securitylevel>
                    <snmpv3_authprotocol>0</snmpv3_authprotocol>
                    <snmpv3_authpassphrase/>
                    <snmpv3_privprotocol>0</snmpv3_privprotocol>
                    <snmpv3_privpassphrase/>
                    <formula>0.01</formula>
                    <delay_flex/>
                    <params/>
                    <ipmi_sensor/>
                    <data_type>0</data_type>
                    <authtype>0</authtype>
                    <username/>
                    <password/>
                    <publickey/>
                    <privatekey/>
                    <port>{$SNMP_PORT}</port>
                    <description/>
                    <inventory_link>0</inventory_link>
                    <applications>
                        <application>
                            <name>General</name>
                        </application>
                    </applications>
                    <valuemap/>
                    <logtimefmt/>
                </item>""")


templatesFim="""            </items>
            <discovery_rules/>
            <macros/>
            <templates/>
            <screens/>
        </template>
    </templates>"""
print(templatesFim)



triggerIni="""    <triggers>"""
print(triggerIni)

#            <expression>{{Template SNMP HP v1910-48G:ifInErrors.{p}.last()}}&gt;100</expression>
triggerCRCRx="""        <trigger>
            <expression>{{Template SNMP HP v1910-48G:ifInErrors.{p}.last(0)}}&gt;100</expression>
            <name>CRC Errors Rx on port {p}</name>
            <url/>
            <status>0</status>
            <priority>4</priority>
            <description/>
            <type>0</type>
            <dependencies/>
        </trigger>"""
for port in range(1,49):
	print(triggerCRCRx.format(p=port))

triggerCRCTx="""       <trigger>
            <expression>{{Template SNMP HP v1910-48G:ifOutErrors.{p}.last(0)}}&gt;100</expression>
            <name>CRC Errors Tx on port {p}</name>
            <url/>
            <status>0</status>
            <priority>4</priority>
            <description/>
            <type>0</type>
            <dependencies/>
        </trigger>"""
for port in range(1,49):
	print(triggerCRCTx.format(p=port))


triggerPortStatus="""        <trigger>
            <expression>{{Template SNMP HP v1910-48G:ifOperStatus.{p}.last(0)}}=2</expression>
            <name>Port {p} status down on {{HOSTNAME}}</name>
            <url/>
            <status>1</status>
            <priority>1</priority>
            <description/>
            <type>0</type>
            <dependencies/>
        </trigger>"""
for port in range(1,49):
	print(triggerPortStatus.format(p=port))

print("""        <trigger>
            <expression>{Template SNMP HP v1910-48G:Uptime.last(0)}&lt;600</expression>
            <name>{HOSTNAME} has just been restarted</name>
            <url/>
            <status>0</status>
            <priority>3</priority>
            <description/>
            <type>0</type>
            <dependencies/>
        </trigger>""")

triggerFim="""    </triggers>"""
print(triggerFim)


print("    <graphs>")
graphItem="""        <graph>
            <name>Port {p} stats</name>
            <width>900</width>
            <height>200</height>
            <yaxismin>0.0000</yaxismin>
            <yaxismax>100.0000</yaxismax>
            <show_work_period>1</show_work_period>
            <show_triggers>1</show_triggers>
            <type>0</type>
            <show_legend>1</show_legend>
            <show_3d>0</show_3d>
            <percent_left>0.0000</percent_left>
            <percent_right>0.0000</percent_right>
            <ymin_type_1>1</ymin_type_1>
            <ymax_type_1>0</ymax_type_1>
            <ymin_item_1>0</ymin_item_1>
            <ymax_item_1>0</ymax_item_1>
            <graph_items>
                <graph_item>
                    <sortorder>0</sortorder>
                    <drawtype>0</drawtype>
                    <color>000099</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template SNMP HP v1910-48G</host>
                        <key>ifOutOctets.{p}</key>
                    </item>
                </graph_item>
                <graph_item>
                    <sortorder>1</sortorder>
                    <drawtype>0</drawtype>
                    <color>990000</color>
                    <yaxisside>0</yaxisside>
                    <calc_fnc>2</calc_fnc>
                    <type>0</type>
                    <item>
                        <host>Template SNMP HP v1910-48G</host>
                        <key>ifInOctets.{p}</key>
                    </item>
                </graph_item>
            </graph_items>
        </graph>"""
for port in range(1,49):
	print(graphItem.format(p=port))

graphFim="""    </graphs>
</zabbix_export>"""
print(graphFim)
