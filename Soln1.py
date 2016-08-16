
# coding: utf-8

# In[ ]:

if __name__ == "__main__":
    main()
    from math import pi

    G = 6.67E-11
    M = 5.97E24
    R = 6371E3

    T = float(input('Enter seconds: '))
    h = ((G*M*T*T/(4*(pi**2)))**(1.0/3)) - R
    print 'The altitude relative to the surface of the Earth that the satellite must have is', h, 'meters'

    print 'For satellites:'
    geos = ((G*M*(86400**2)/(4*(pi**2)))**(1.0/3)) - R
    print '--> at the geosynchronous orbit, the altitude is', geos, 'meters'
    s_90 = ((G*M*(5400**2)/(4*(pi**2)))**(1.0/3)) - R
    print '--> orbiting once every 90 minutes, the altitude is', s_90, 'meters'
    s_45 = ((G*M*(2700**2)/(4*(pi**2)))**(1.0/3)) - R
    print '--> orbiting once every 45 minutes, the altitude is', s_45, 'meters'

    real_geos = ((G*M*(86148**2)/(4*(pi**2)))**(1.0/3)) - R
    diff = geos - real_geos
    per = (real_geos/geos)*100
    print(per)

    print('')
    print 'But if we use the exact orbit time of a geosynchronous satellite, the altitude would be', real_geos, 'meters'
    print 'This value is', per, 'percent ( less than', diff,')of the value of time when a full 24 hours for the time is used.'

