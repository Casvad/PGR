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
		##PCS
        PC1 = self.addHost('PC1')
        PC2 = self.addHost('PC2')
        PC3 = self.addHost('PC3')
        PC4 = self.addHost('PC4')
        PC5 = self.addHost('PC5')
        PC6 = self.addHost('PC6')
		##Phones
        Phone1 = self.addHost('Phone1')
        Phone2 = self.addHost('Phone2')
        Phone3 = self.addHost('Phone3')
        Phone4 = self.addHost('Phone4')
		##Laptops
        Laptop1 = self.addHost('Laptop1')
        Laptop2 = self.addHost('Laptop2')
        Laptop3 = self.addHost('Laptop3')
        Laptop4 = self.addHost('Laptop4')

        # Add servers

        Inv = self.addHost('Inv')
        Des = self.addHost('Des')
        Pruebas = self.addHost('Pruebas')
        
        # Add switches

        Core1 = self.addSwitch('Core1')
        Core2 = self.addSwitch('Core2')

        Dist1 = self.addSwitch('Dist1')
        Dist2 = self.addSwitch('Dist')
        Dist3 = self.addSwitch('Dist3')
        Dist4 = self.addSwitch('Dist4')

        Access1 = self.addSwitch('Access1')
        Access2 = self.addSwitch('Access2')
        Access3 = self.addSwitch('Access3')
        Access4 = self.addSwitch('Access4')

        # Add links
        ##Between Switchs

        self.addLink(Core1,Core2)

        self.addLink(Core1,Dist1)
        self.addLink(Core1,Dist2)
        self.addLink(Core1,Dist3)
        self.addLink(Core1,Dist4)

        self.addLink(Core2,Dist1)
        self.addLink(Core2,Dist2)
        self.addLink(Core2,Dist3)
        self.addLink(Core2,Dist4)

        self.addLink(Dist1,Access1)
        self.addLink(Dist2,Access2)
        self.addLink(Dist3,Access3)
        self.addLink(Dist4,Access4)

        ##Between Switch-Server

        self.addLink(Access4,Inv)
        self.addLink(Access4,Des)
        self.addLink(Access4,Pruebas)

        ##Between Switch-Host

        self.addLink(Access1,PC1)
        self.addLink(Access1,PC2)
        self.addLink(Access1,PC3)
        self.addLink(Access1,Phone1)
        self.addLink(Access1,Phone2)

        self.addLink(Access2,Laptop1)
        self.addLink(Access2,Laptop2)
        self.addLink(Access2,PC4)
        self.addLink(Access2,PC5)
        self.addLink(Access2,PC6)

        self.addLink(Access3,Phone3)
        self.addLink(Access3,Phone4)
        self.addLink(Access3,Laptop3)
        self.addLink(Access3,Laptop4)

topos = { 'PgrTopo': ( lambda: PgrTopo() ) }
