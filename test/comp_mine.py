from __future__ import absolute_import, division, print_function

def comp(filename):

    def readfile(ff):
        data = []
        fh = open(ff)
        for line in fh:
            ss = line.split()
            if("REMARK" in line): continue
            if(len(ss)!=0):
                vv = []
                for el in ss:
                    if(el=="nan"):
                        vv.append(el)
                    else:
                        try:
                            vv.append(float(el))
                        except:
                            vv.append(el)
                data.append(vv)
        fh.close()
        return data
    
    ref = readfile(filename)
    cur = readfile(filename.replace("reference","tmp"))
    assert len(ref)==len(cur), "reference and test files %s have different shapes " % filename.split("/")[-1]
    for el1,el2 in zip(ref,cur):
        assert len(el1)==len(el2), "reference and test files %s have different shapes " % filename.split("/")[-1]
        for it1,it2 in zip(el1,el2):
            if(str(it1)[:4]=="srel"):
                it1=float(str(it1).split("=")[1])
                it2=float(str(it2).split("=")[1])
                assert (it1-it2)**2<1.E-04, "reference and test files %s give different results %10.4e %10.4e " % (filename.split("/")[-1],it1,it2)
            elif(type(it1)==float):
                assert (it1-it2)**2<1.E-04, "reference and test files %s give different results %10.4e %10.4e " % (filename.split("/")[-1],it1,it2)
            else:
                assert it1==it2, "reference and test files %s give different results %s %s" % (filename.split("/")[-1],it1,it2)
