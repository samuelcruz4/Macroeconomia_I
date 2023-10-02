# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:02:50 2023

@author: savia
"""

import numpy as np
import matplotlib.pyplot as plt
###########################################################################
# Funções
###########################################################################
def util(x):
    # return ( x**(1-sigma) -1)/(1-sigma)
    return ( x**(1-sigma) -1)/(1-sigma)
###########################################################################
def define_parameters_and_objects():
    global beta, rho, sigma, r, w, delta, alpha, pi, y_grid,\
            a_grid, n_y, n_a, V, iG, Tr, tau, L
    
    sigma, r = 2, 0.05
    beta = .9
    rho = beta**(-1)-1
    delta, alpha = 0.04, 0.3
    Tr, tau = 0, 0
#    k = (alpha/r)**(1/(1-alpha))
#    w = (1-alpha)*(k**alpha)
    
    pi = np.array([
                    [2/3, 1/3],
                    [1/3, 2/3]
                    ])
    y_min, y_max, n_y = 1e-2, 1, len(pi)
    y_grid = np.linspace(y_min, y_max, n_y)
    
    barA, a_max, n_a = 0, 20, 150
    a_grid = np.linspace(-barA, a_max, n_a)
    
    V = np.zeros( (n_y, n_a) )
    iG = np.zeros( (n_y, n_a) , dtype=np.int )
    
    L = compute_Ey()
###########################################################################
def compute_Ey():
    barPI = compute_barPI()
    Ey = 0
    for i_y, y in enumerate(y_grid):
        mea = barPI[i_y]
        lab = y
        Ey += lab*mea
    return Ey
###########################################################################
def compute_barPI():
    barPI = np.ones( n_y )/n_y
    norm_pi, tol_pi = 1, 1e-12
    while norm_pi>tol_pi:
        T_barPI = np.dot(barPI, pi)
        norm_pi = max(abs(T_barPI-barPI))
        barPI = T_barPI/sum(T_barPI)
    return barPI
###########################################################################
def build_objective(V, r):
    global w, Tr, tau
    k = compute_k(r)
    w = compute_w(k)
    F_OBJ = np.zeros( (n_y, n_a, n_a) )
    for i_y in range(n_y):
        y = y_grid[i_y]
    #for i_y, y in enumerate(y_grid):
        for i_a, a in enumerate(a_grid):
            for i_aa, aa in enumerate(a_grid):
                c = w*y + (1+(1-tau)*r)*a - aa + Tr
                if c<=0:
                    F_OBJ[i_y, i_a, i_aa] = -np.inf
                else:
                    F_OBJ[i_y, i_a, i_aa] = util(c) + beta*(  np.dot(pi[i_y,:],V[:, i_aa]) )
    return F_OBJ
###########################################################################
def compute_k(r):
    return (alpha/(r+delta))**(1/(1-alpha))
###########################################################################    
def compute_w(k):
    return (1-alpha)*(k**alpha)
###########################################################################
def compute_r(K):
    global L
    return alpha*((K/L)**(alpha-1)) - delta
###########################################################################
def compute_TV_and_TG(F_OBJ):
    TV = np.zeros( (n_y, n_a) )
    T_iG = np.zeros( (n_y, n_a) , dtype=np.int )
    for i_y in range(n_y):
        for i_a in range(n_a):
            TV[i_y, i_a] = np.max(F_OBJ[i_y, i_a, :])
            T_iG[i_y, i_a] = np.argmax(F_OBJ[i_y, i_a, :])
    return TV, T_iG
###########################################################################    
def compute_V_and_G():
    global V, iG, r
    norm, tol = 1, 1e-2
    while norm>tol:
        F_OBJ = build_objective(V, r)
        TV, T_iG = compute_TV_and_TG(F_OBJ)
        norm = np.max(abs(TV-V))
        V = np.copy(TV)
        iG = np.copy(T_iG)
#        print('norm =',norm)
    return V, iG
###########################################################################
def compute_Q(iG):
    # States values
    # [ (y_0, a_0), (y_0, a_1), (y_0, a_2), (y_0, a_3), (y_0, a_4) ,
    #   (y_1, a_0), (y_1, a_1), (y_1, a_2), (y_1, a_3), (y_1, a_4) ]
    Q = np.zeros( (n_y*n_a, n_y*n_a) )
    
    for i_y in range(n_y):
        for i_a in range(n_a):
            c_state = i_y*n_a+i_a
            for i_yy in range(n_y):
                for i_aa in range(n_a):
                    n_state = i_yy*n_a+i_aa
                    if iG[i_y,i_a] == i_aa:
                        Q[c_state, n_state] += pi[i_y,i_yy]
    return Q
###########################################################################
def compute_bar_phi(Q):
    bar_phi = np.ones( n_y*n_a )/(n_y*n_a)
    norm_M, tol_M = 1, 1e-12
    while norm_M>tol_M:
        Tbar_phi = np.dot(bar_phi, Q)
        norm_M = max(abs(Tbar_phi-bar_phi))
        bar_phi = Tbar_phi/sum(Tbar_phi)
    return bar_phi
###########################################################################
def compute_Ea(bar_phi):
    Ea = 0
    for i_y in range(n_y):
        for i_a in range(n_a):
            c_state = i_y*n_a+i_a
            mea = bar_phi[c_state]
            s_index = iG[i_y,i_a]
            sav = a_grid[ s_index ]
            Ea += sav*mea
    return Ea    
###########################################################################
def compute_d(bar_phi):
    k = compute_k(r)
    L = compute_Ey()
    K = k*L
    Ea = compute_Ea(bar_phi)
    d = K - Ea
#    print('(K,Ea,d) = (',K,Ea,d,')')
    return d
###########################################################################
def compute_equilibrium():
    global r, w, V, iG, Q, bar_phi, Tr, tau, L
    r_L, r_H = -delta, rho
    norm_r, tol_r = 1, 1e-12
    while norm_r>tol_r:
        r = (r_L+r_H)/2
        k = compute_k(r)
        Tr = tau*r*k*L
        V, iG = compute_V_and_G()
        Q = compute_Q(iG)
    #    print(Q)
        bar_phi = compute_bar_phi(Q)
    #    print(bar_phi)
        d = compute_d(bar_phi)
        if d>0:
            r_L = r
        elif d<0:
            r_H = r
        norm_r = abs(r_H-r_L)
        # norm_r = max(abs(r_H-r_L),abs(d))
        print('[d,r_L,r_H,norm]=[{:9.6f},{:9.6f},{:9.6f},{:9.6f}]'.format(d,r_L,r_H,norm_r))

###########################################################################
###########################################################################
# Main Code
###########################################################################
###########################################################################
define_parameters_and_objects()    

## 1.
print('\nCalculando o SS inicial')
tau = 0
compute_equilibrium()
phi_0 = np.copy(bar_phi)
V_0 = np.copy(V)
iG_0 = np.copy(iG)
r_0 = np.copy(r)
w_0 = np.copy(w)
Tr_0 = np.copy(Tr)
K_0 = compute_Ea(phi_0)

plt.plot(a_grid,V_0[0,:])
plt.plot(a_grid,V_0[1,:])
plt.show()


G_0 = a_grid[iG_0]
plt.plot(a_grid,G_0[0,:])
plt.plot(a_grid,G_0[1,:])
plt.plot(a_grid, a_grid)
plt.show()

## 2.
print('\nCalculando o SS final')
tau = 0.05
compute_equilibrium()
Phi_inf = np.copy(bar_phi)
V_inf = np.copy(V)
iG_inf = np.copy(iG)
r_inf = np.copy(r)
w_inf = np.copy(w)
Tr_inf = np.copy(Tr)
K_inf = compute_Ea(Phi_inf)

plt.plot(a_grid,V_inf[0,:])
plt.plot(a_grid,V_inf[1,:])
plt.show()


G_inf = a_grid[iG_inf]
plt.plot(a_grid,G_inf[0,:])
plt.plot(a_grid,G_inf[1,:])
plt.plot(a_grid, a_grid)
plt.show()

## 3.
N = 0
norm_Phi, tol_Phi = 1, 1e-5
while (norm_Phi>tol_Phi):
    N += 10
    ## 4.
    K_path = np.ones(N)
    for t in range(N):
        K_path[t] = ( K_inf*t+K_0*(N-1-t) )/(N-1)
#    print(K_path)
    # fig, ax = plt.subplots()
    # ax.plot(range(N), K_path,'-o')
    
    norm_K_path, tol_K_path = 1, 1e-3
       ## 5.
    while (norm_K_path>tol_K_path):
        r_path, w_path, Tr_path = np.ones(N), np.ones(N), np.ones(N)
        for t in range(N):
            r_path[t] = compute_r( K_path[t] )
            w_path[t] = compute_w( K_path[t] / L )
            Tr_path[t] = tau*r_path[t]*K_path[t]
            
        
            
        # fig, ax = plt.subplots(2,2, figsize=(12,9))
        # t_grid = [t+1 for t in range(N)]
        # ax[0,0].plot(t_grid,K_path,'o-')
        # ax[0,1].plot(t_grid,r_path,'o-')
        # ax[1,0].plot(t_grid,w_path,'o-')
        # ax[1,1].plot(t_grid,Tr_path,'o-')
        # plt.show()
        
        ## 6.
        V_path = np.zeros( (n_y, n_a, N) )
        V_path[:,:,N-1] = V_inf
        iG_path = np.zeros( (n_y, n_a, N), dtype=np.int )
        iG_path[:,:,N-1] = iG_inf
        plt.plot(a_grid, V_path[0,:,N-1])
        
        for t in range(N,1,-1):
            # print(t)
            V = V_path[:,:,t-1]
            r = r_path[t-2]
            w = w_path[t-2]
            Tr = Tr_path[t-2]
            
            F_OBJ = build_objective(V, r)
            V, iG = compute_TV_and_TG(F_OBJ)
            
            V_path[:,:,t-2] = V
            iG_path[:,:,t-2] = iG
            plt.plot(a_grid, V_path[0,:,t-2])
        ## 7.
        Gamma_path = np.zeros( (n_y*n_a, n_y*n_a, N) )
        for t in range(N):
            iG = iG_path[:,:,t]
            Gamma_path[:,:,t] = compute_Q(iG)
            
        phi_path = np.zeros( (N, n_y*n_a) )
        phi_path[0,:] = phi_0
        for t in range(1,N):
            # print(t)
            Phi_t = phi_path[t-1,:]
            Gamma_t = Gamma_path[:,:,t-1]
            phi_path[t,:] = np.dot(Phi_t, Gamma_t)
        
        ## 8.
        A_path = np.zeros( N )
        #A_path[t] = compute_Ea()
        
        for t in range(N):
            Ea_t = 0
            for i_y in range(n_y):
                for i_a in range(n_a):
                    c_state = i_y*n_a+i_a
                    Phi_t = phi_path[t,:]
                    mea = Phi_t[c_state]
                    # iG_t = iG_path[:,:,t]
                    # s_index = iG_t[i_y,i_a]
                    a = a_grid[ i_a ]
                    Ea_t += a*mea
            A_path[t] = Ea_t
            
        # print('\nTrajetória de Capital:\n',K_path)
        # print('\nTrajetória de Poupança:\n',A_path)
        fig, ax = plt.subplots()
        t_grid = [t+1 for t in range(N)]
        ax.plot([1-i for i in range(5)], [K_0 for i in range(5)],'o',label='$K_0$')
        ax.plot(t_grid, K_path,'-o',label='$K_t$')
        ax.plot(t_grid, A_path,'--s',label='$A_t$')
        ax.set_xlabel('Time $t$')
        ax.plot([N+i for i in range(5)], [K_inf for i in range(5)],'x',label='$K_\infty$')
        plt.legend(loc='best')
        plt.show()
        
        ## 9.
        norm_K_path = np.max([abs(A_path[ii]-K_path[ii]) for ii in range(N)])
        # norm_K_path = np.max([abs(A_path[ii]-K_path[ii]) for ii in range(N-1)])
        print('Norma da trajetória de Capital:',norm_K_path)
        mu = .5
        for ii in range(1,N):
        # for ii in range(1,N-1):
            # print(ii)
            K_path[ii] = (mu*K_path[ii]+(1-mu)*A_path[ii])

    ## 10.
    norm_Phi = np.max(abs(phi_path[N-1,:]-Phi_inf))
    print('Norma da distribuição final:',norm_Phi,N,'\n')