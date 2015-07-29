/*******************
    Akash Agrawall
    IIIT HYDERABAD
    ***********************/
 
 
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<climits>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<stack>
#include<queue>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<functional>
#include<numeric>
using namespace std;
#define pb push_back
#define sz(x) int(x.size())
#define mp make_pair
#define fill(x,v) memset(x,v,sizeof(x))
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d ",n)
#define pd(n) printf("%lf ",n);
#define pdl(n) printf("%lf\n",n);
#define pin(n) printf("%d\n",n)
#define pln(n) printf("%lld\n",n)
#define pl(n) printf("%lld ",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define scan(v,n) vector<int> v;rep(i,n){ int j;si(j);v.pb(j);}
#define mod (int)(1e9 + 7)
#define ll long long int
#define F first
#define S second
ll modpow(ll a,ll n,ll temp){ll res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;} 
ll arr[100006],flagit[134],flg[134];
inline ll checkit(ll calc)
{
    if(calc>=mod)
        calc%=mod;
    return calc;
}
inline ll chck(ll calc)
{
    while(calc<0)
        calc+=mod;
    calc%=mod;
    return calc;
}
int main()
{
    ll n,calc,calc1,i,j,sz,c1,c2,ans=0;
    sl(n);
    rep(i,n)
    {
        sl(arr[i]);
    }
    rep(i,135)
        flagit[i]=0;
    rep(i,n)
    {
        rep(j,135)
            flg[j]=0;
        rep(j,129)
        {
            if(flagit[j]!=0)
            {
                calc=j^arr[i];
                //printf("i=%d j=%d calc=%d\n",i,j,calc);
                flg[calc]+=flagit[j];
                flg[calc]=checkit(flg[calc]);
            }
        }
        rep(j,129)
        {
            //printf("i=%d calc=%d calc1=%d\n",i,calc,calc1);
            flagit[j]+=flg[j];
            flagit[j]=checkit(flagit[j]);
        }
        flagit[arr[i]]++;
        flagit[arr[i]]=checkit(flagit[arr[i]]);
    }
    c2=modpow(2,mod-2,mod);
    //pln(c2);
    rep(i,129)
    {
        //printf("i=%d flagit=%d\n",i,flagit[i]);
        calc=flagit[i];
        c1=calc*(calc-1);
        c1=chck(c1);
        c1=c1*c2;
        c1=checkit(c1);
        ans+=c1;
        ans=checkit(ans);
    }
    pln(ans);
    return 0;
}

