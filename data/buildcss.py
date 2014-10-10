hi = ['hll','c','er','k','o','cm','cp','c1','cs','gd','ge','gr','gh','gi','go','gp','gs','gu','gt','kc','kd','kn','kp','kr','kt','m','s','na','nb','nc','no','nd','ni','ne','nf','nl','nn','nt','nv','ow','w','mf','mh','mi','mo','sb','sc','sd','s2','se','sh','si','sx','sr','s1','ss','bp','vc','vg','vi','il']

for h in hi:
    print ('.{0} {{ color:$col-{0}; background-color:$gb-{0}; font-weight:$w-{0} }}'.format(h))
