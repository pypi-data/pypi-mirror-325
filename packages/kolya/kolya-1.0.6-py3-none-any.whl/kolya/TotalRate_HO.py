from kolya import parameters
import math

def X_Gamma_KIN_MS_HO(par, hqe, flagmb4 = 1, flagmb5 = 1):
    r=par.mcMS/par.mbkin
    mu0=par.scale_mcMS/par.mbkin
    mus=par.scale_alphas/par.mbkin
    muWC=par.scale_mbkin/par.mbkin
    mumuG=par.scale_muG/par.mbkin
    api=par.alphas/math.pi

    rhoD=hqe.rhoD/par.mbkin**3
    rhoLS=hqe.rhoLS/par.mbkin**3
    muG=hqe.muG/par.mbkin**2
    mupi=hqe.mupi/par.mbkin**2

    m1=hqe.m1/par.mbkin**4
    m2=hqe.m2/par.mbkin**4
    m3=hqe.m3/par.mbkin**4
    m4=hqe.m4/par.mbkin**4
    m5=hqe.m5/par.mbkin**4
    m6=hqe.m6/par.mbkin**4
    m7=hqe.m7/par.mbkin**4
    m8=hqe.m8/par.mbkin**4
    m9=hqe.m9/par.mbkin**4
    r1=hqe.r1/par.mbkin**5
    r2=hqe.r2/par.mbkin**5
    r3=hqe.r3/par.mbkin**5
    r4=hqe.r4/par.mbkin**5
    r5=hqe.r5/par.mbkin**5
    r6=hqe.r6/par.mbkin**5
    r7=hqe.r7/par.mbkin**5
    r8=hqe.r8/par.mbkin**5
    r9=hqe.r9/par.mbkin**5
    r10=hqe.r10/par.mbkin**5
    r11=hqe.r11/par.mbkin**5
    r12=hqe.r12/par.mbkin**5
    r13=hqe.r13/par.mbkin**5
    r14=hqe.r14/par.mbkin**5
    r15=hqe.r15/par.mbkin**5
    r16=hqe.r16/par.mbkin**5
    r17=hqe.r17/par.mbkin**5
    r18=hqe.r18/par.mbkin**5

    res = 0

    if flagmb4 == 1:
        res += m1*((1./8.)-r**2+r**6-(r**8)/8.-2.*((3./2.)*r**4)*math.log(r))
        res += (m2/72.)*(-533.+1032.*r**2-720.*r**4+56.*r**6+165.*r**8-24.*(8.+27.*r**4)*math.log(r))
        res += m3*((13./9.)-4.*r**2+8.*r**4-(76./9.)*r**6+3*r**8+(8./3.)*math.log(r))
        res += (m4/24.)*(-67.+56.*r**2+48.*r**4-56.*r**6+19.*r**8-24.*(4.+r**4)*math.log(r))
        res += (m5/72.)*(-397.+744.*r**2-1008.*r**4+856.*r**6-195.*r**8-24.*(16.+27.*r**4)*math.log(r))
        res += m6*((257./72.)-5.*r**2-4.*r**4+(77./9.)*r**6-(25./8.)*r**8-(1./3.)*(-8.+9.*r**4)*math.log(r))
        res += m7*0
        res += (m8/32.)*(1.-8.*r**2+8.*r**6-r**8-(24.*r**4)*math.log(r))
        res += (m9/18.)*(-25.+48.*r**2-36.*r**4+16.*r**6-3.*r**8-24.*math.log(r))
    if flagmb5 == 1:
        res += (r1/360.)*(-1127.-840.*r**2-2736.*r**4+11720.*r**6-7017.*r**8-120.*(4.+9.*r**4)*math.log(r))
        res += (2.*r2/15.)*(40.-(51./r**2)-20.*r**2+30.*r**4+35.*r**6-34.*r**8+30.*(-7.+3.*r**4)*math.log(r))
        res += (r3/90.)*(-835.+(648./r**2)+480.*r**2-1620.*r**4+1960.*r**6-633.*r**8-120.*(-10.+9.*r**4)*math.log(r))
        res += r4*((131./9.)-(34./(5.*r**2))-8.*r**2+16.*r**4-(230.*r**6/9.)+(49.*r**8/5.)+(2./3.+6.*r**4)*2*math.log(r))
        res += (r5/360.)*(485.+(576./r**2)-600.*r**2-1800.*r**4+1720.*r**6-381.*r**8-120.*(-28.+9.*r**4)*math.log(r))
        res += (r6/360.)*(-2875.+(1296./r**2)+1320.*r**2+1080.*r**4 - 2840.*r**6 + 2019.*r**8 -120.* (20. + 9.*r**4)*math.log(r))
        res += (r7/360.)*(35. - (144./r**2) + 600.*r**2 + 360.*r**4 + 280.*r**6 - 1131.*r**8 + 120.*(28. + 9.*r**4)*math.log(r))
        res += (r8/72.)*(197. - 744.*r**2 + 144.*r**4 + 1000.*r**6 - 597.*r**8 - 24.*(4. + 9.*r**4)*math.log(r))
        res += ((r9*(12+19*r**2-60*r**4+132*r**6-136*r**8+33*r**10+12*r**2*(5+9*r**4)*math.log(r)))/(9*r**2))
        res += ((r10*(-157+36/r**2+72*r**2+108*r**4+4*r**6-63*r**8+24*(-10+9*r**4)*math.log(r)))/18)
        res += (-1/18*(r11*(12-253*r**2+288*r**4+276*r**6-476*r**8+153*r**10+24*r**2*(-10+9*r**4)*math.log(r)))/r**2)
        res += (-1/18*(r12*(36+5*r**2-96*r**4+396*r**6-500*r**8+159*r**10+24*r**2*(8+9*r**4)*math.log(r)))/r**2)
        res += ((r13*(24-187*r**2+216*r**4+228*r**6-416*r**8+135*r**10+24*r**2*(-4+9*r**4)*math.log(r)))/(18*r**2))
        res += (r14/9.)*(13. + (6./r**2) - 36.*r**2 + 156.*r**4 - 202.*r**6 + 63.*r**8 + 12.*(5. + 9.*r**4)*math.log(r))
        res += ((r15*(-16+75*r**2-40*r**4-56*r**6+24*r**8+13*r**10+(96*r**2-72*r**6)*math.log(r)))/(12*r**2))
        res += ((r16*(-48+521*r**2-408*r**4-168*r**6-152*r**8+255*r**10-24*r**2*(-20+9*r**4)*math.log(r)))/(72*r**2))
        res += (r17/24.)*(-77. + 184.*r**2 - 120.*r**4 - 88.*r**6 + 101.*r**8 - 24.*(4. + 3.*r**4)*math.log(r))
        res += (-1/36*(r18*(-24+245*r**2-120*r**4-120*r**6-272*r**8+291*r**10-24*r**2*(-8+9*r**4)*math.log(r)))/r**2)

    return res
