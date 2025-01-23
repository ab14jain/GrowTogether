#include <vector>
#include <set>
#include <iostream>
#define ll long long
class Solution {
    public:
    
        long long mod_inv(long long a,long long n,long long p)
        {   long long res=1;
            while(n)
            { if(n%2)
                {
                    res=(res*a)%p;
                    n--;
                }
                else
                {
                    a=(a*a)%p;
                    n/=2;
                }
            }
            return res;
        }

        std::vector<int> getFinalState(std::vector<int>& nums, int k, int multiplier) 
        {   
            if(multiplier==1)
            {
                return nums;
            } 
            ll mod=1000000007;
            int n=nums.size();
            std::set<std::pair<ll,int>>st;
            std::vector<std::pair<ll,int>>vp; 
            for(int i=0;i<nums.size();i++)
            {
                st.insert({nums[i],i});
            }
           
            for(auto it=st.begin();it!=st.end();it++)
            {
                std::cout << (*it).first;
                std::cout << " " << (*it).second;
                std::cout << "\n";
                
            }
            std::cout << "======End====\n";

            while(k)
            {
                auto firstit=st.begin();
                auto lastit=st.end();
                lastit--;
                if(((*firstit).first*multiplier)>(*lastit).first)
                {
                    break;
                }
                else
                {  
                    ll ind=(*firstit).second;
                    ll val=((*firstit).first*multiplier)%mod;
                    st.erase(firstit);
                    st.insert({val,ind});
                }
                k--;
            }
            std::cout << "======While Start====\n";
            for(auto it=st.begin();it!=st.end();it++)
            {
                std::cout << (*it).first;
                std::cout << " " << (*it).second;
                std::cout << "\n";             
                
            }
            std::cout << "======While End====\n";
            for(auto it=st.begin();it!=st.end();it++)
            {
                vp.push_back(*it);
                
            }

            std::cout << "======vp While Start====\n";
            for(int i=0;i<vp.size();i++)
            {
                std::cout << vp[i].first;
                std::cout << " " << vp[i].second;
                std::cout << "\n";
                
                
            }
            std::cout << "======vp While End====\n";
        
            for(int i=0;i<vp.size();i++)
            {
                ll value=mod_inv(multiplier,k/n,mod)%mod;
                // std::cout << value;
                // std::cout << "\n";
                vp[i].first=((vp[i].first*value)%mod);
            }
            std::cout << "======Full====\n";
            for(int i=0;i<vp.size();i++)
            {
                std::cout << vp[i].first;
                std::cout << "\n";
                std::cout << "i=" << vp[i].second << "\n";
            }
            std::cout << "======Full====\n";

            int extra=k%n;
            std::cout << extra << " extra\n";
            std::cout << multiplier << " multiplier\n";
            for(int i=0;i<extra;i++)
            {
                std::cout << vp[i].first;
                std::cout << "\n";
                ll calc = (vp[i].first*multiplier)%mod;
                vp[i].first = calc;
                std::cout << calc;
                std::cout << "i=" << vp[i].second << "\n";
            }

            std::cout << "========== extra ========\n";
            for(int i=0;i<vp.size();i++)
            {
                std::cout << vp[i].first;
                std::cout << "\n";
            }
            std::cout << "========== extra ========\n";

            std::vector<int>ans(n,0);
            for(int i=0;i<n;i++)
            {
                ans[vp[i].second]=vp[i].first;
            }
            return ans;
        }

};

//instantiate the class and call the function c++

int main() {
    Solution *s = new Solution();
    // std::vector<int> nums={7,8,9,10,11};
    // std::vector<int> nums={889458628,338743558,875422936,684907163,233489834};
    // int k=246181588;
    // int multiplier=313380;
    // std::vector<int> nums={1,2,3,4,5};
    std::vector<int> nums={5,4,3,2,1};
    int k=300;
    int multiplier=2;
    std::vector<int> result = s->getFinalState(nums,k,multiplier);

    for(int i : result) {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    delete s;
    return 0;
}


