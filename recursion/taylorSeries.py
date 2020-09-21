p=1
f=1
class Series:
    p=1
    f=1
    s=1
    def series1(self, x, n):
        if n<1:
            return 1
        else:
            print(n)
            r = self.series1(x,n-1)

            Series.p = Series.p*x
            Series.f = Series.f*n
            return r+Series.p/Series.f

    def series2(self, x, n):
        
        if n == 0:
            return Series.s
        Series.s = 1+x*Series.s/n
        return self.series2(x, n-1)
    


series = Series()
print(series.series1(2,10))
print(series.series2(1,4))