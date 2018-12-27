import numpy as np
class CRR():
    def __init__(self,S0,u,d,K,r,T):
        if u&lt;=d :
            print (&quot;error&quot;)
        else :
            self.S0=S0 
            self.u=u
            self.d=d
            self.K=K
            self.r=r
            self.T=T
            [self.a,self.b]=self.uneEtape()
            self.sigma=self.a*self.S0 + self.b
        
        
    def uneEtape(self):
        a= (self.S0*self.u -self.K) / (self.S0 *(self.u-self.d))
        b= - (a *self.S0*self.d)*np.exp(- self.r*self.T)
        return [a,b]
    def infos(self):
        prixAchat = self.a*self.S0
        valeur1 = self.a*self.S0*self.u
        valeur2 = self.a*self.S0*self.d
        valeurEcheance=[valeur1,valeur2]
        valeurP=self.S0*self.u - self.K
        return (&quot;on trouve a = &quot;,self.a ,&quot;, b = &quot;, self.b , &quot; et donc la valeur C0= sigma sera&quot; , self.sigma , &quot; donc le prix d&#39;achat propose sera&quot;, prixAchat ,&quot;et la valeur d&#39;echance est soit&quot;,valeurEcheance,&quot;donc dans le 1er cas il paeira &quot;,valeurP,&quot;et il rembourse &quot;,-self.b, &quot;avec des interets r=0,  et dans le 2eme cas il remboursera donc les &quot;,- self.b,)
z =CRR(120,1.5,0.5,80,0,1) 
z.uneEtape()
print(z.sigma)
z.infos()
