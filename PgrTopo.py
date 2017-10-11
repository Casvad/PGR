"""Custom topology for PGR1-SDN

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=PgrTopo' from the command line.
"""

from mininet.topo import Topo

class PgrTopo( Topo ):
    "PGR1-SDN Topology"
    def __init__( self ):
        "Create custom topo"
        
        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        PC1 = self.addHost('PC1')
        PC2 = self.addHost('PC2')
        PC3 = self.addHost('PC3')
        PC4 = self.addHost('PC4')
        PC5 = self.addHost('PC5')
        PC6 = self.addHost('PC6')
        PC7 = self.addHost('PC7')
        PC8 = self.addHost('PC8')
        PC9 = self.addHost('PC9')
        PC10 = self.addHost('PC10')
        PC11 = self.addHost('PC11')
        PC12 = self.addHost('PC12')
        PC13 = self.addHost('PC13')
        PC14 = self.addHost('PC14')
        PC15 = self.addHost('PC15')
        PC16 = self.addHost('PC16')
        PC17 = self.addHost('PC17')
        PC18 = self.addHost('PC18')

        # Add servers

        Investigacion = self.addHost('Investigacion')
        Desarrollo = self.addHost('Desarrollo')
        Pruebas = self.addHost('Pruebas')
        
        # Add switches

        Core1 = self.addSwitch('Core1')
        Core2 = self.addSwitch('Core2')

        Distribution1 = self.addSwitch('Distribution1')
        Distribution2 = self.addSwitch('Distribution2')
        Distribution3 = self.addSwitch('Distribution3')
        Distribution4 = self.addSwitch('Distribution4')

        Access1 = self.addSwitch('Access1')
        Access2 = self.addSwitch('Access2')
        Access3 = self.addSwitch('Access3')
        Access4 = self.addSwitch('Access4')

        # Add links
        ##Between Switchs

        self.addLink(Core1,Core2)

        self.addLink(Core1,Distribution1)
        self.addLink(Core1,Distribution2)
        self.addLink(Core1,Distribution3)
        self.addLink(Core1,Distribution4)

        self.addLink(Core2,Distribution1)
        self.addLink(Core2,Distribution2)
        self.addLink(Core2,Distribution3)
        self.addLink(Core2,Distribution4)

        self.addLink(Distribution1,Access1)
        self.addLink(Distribution2,Access2)
        self.addLink(Distribution3,Access3)
        self.addLink(Distribution4,Access4)

        ##Between Switch-Server

        self.addLink(Access4,Investigacion)
        self.addLink(Access4,Desarrollo)
        self.addLink(Access4,Pruebas)

        ##Between Switch-Host

        self.addLink(Access1,PC1)
        self.addLink(Access1,PC2)
        self.addLink(Access1,PC3)
        self.addLink(Access1,PC4)
        self.addLink(Access1,PC5)
        self.addLink(Access1,PC6)

        self.addLink(Access2,PC7)
        self.addLink(Access2,PC8)
        self.addLink(Access2,PC9)
        self.addLink(Access2,PC10)
        self.addLink(Access2,PC11)
        self.addLink(Access2,PC12)

        self.addLink(Access3,PC13)
        self.addLink(Access3,PC14)
        self.addLink(Access3,PC15)
        self.addLink(Access3,PC16)
        self.addLink(Access3,PC17)
        self.addLink(Access3,PC18)

topos = { 'PgrTopo': ( lambda: PgrTopo() ) }
