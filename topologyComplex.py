#!/usr/bin/python

from mininet.node import Host, CPULimitedHost, Node
from mininet.node import OVSKernelSwitch
from mininet.topo import Topo

class TopologyComplex(Topo):

    def __init__(self):
        Topo.__init__(self)
        #Add hosts
        h7 = self.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
        h8 = self.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
        h1 = self.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
        h2 = self.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
        h4 = self.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
        h3 = self.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
        h5 = self.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
        h6 = self.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
        h9 = self.addHost('h9', cls=Host, ip='10.0.0.7', defaultRoute=None)

        #Add switches
        s1 = self.addSwitch('s1', cls=OVSKernelSwitch)
        s2 = self.addSwitch('s2', cls=OVSKernelSwitch)
        s3 = self.addSwitch('s3', cls=OVSKernelSwitch)
        s4 = self.addSwitch('s4', cls=OVSKernelSwitch)

        #Add links
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

        self.addLink(h4, s2)
        self.addLink(h5, s2)
        self.addLink(h6, s2)

        self.addLink(h7, s3)
        self.addLink(h8, s3)
        self.addLink(h9, s3)

        self.addLink(s1, s4)
        self.addLink(s2, s4)
        self.addLink(s3, s4)

topos = { 'mytopo': (lambda: TopologyComplex() ) }
