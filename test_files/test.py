5/0

def Psat(self, T):
    pop= self.getPborder(T)
    boolean=int(pop[0])
   
    P1=pop[1]
    P2=pop[2]
    if boolean:
        Pmin = float(min([P1, P2]))
        Pmax = float(max([P1, P2]))
        Tr=T/self.typeMolecule.Tc
        w=0.5*(1+scipy.tanh((10**5)*(Tr-0.6)))
        fi1=0.5*(1-scipy.tanh(8*((Tr**0.4)-1)))
        fi2=0.460*scipy.sqrt(1-(Tr-0.566)**2/(0.434**2)+0.494

        guess = Pmin+(Pmax-Pmin)*((1-w**2)*fi1+(w**2)*fi2)   # error here
    
        solution = scipy.optimize.newton(funcPsat,guess, args=(T,self))
