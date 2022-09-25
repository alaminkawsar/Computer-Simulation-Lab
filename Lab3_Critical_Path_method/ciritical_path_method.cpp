#include<bits/stdc++.h>
using namespace std;

vector<int>adj[105];
int duration[105];

struct Node{
    int ES=INT_MAX,EF=0,LS=0,LF=0;
    int duration = 0;
}Graph[105];
int vis[105];


int dfs(int node, int ES, int EF,int LS, int LF){
    if(adj[node].size()==0){
        
        return 0;
    }
    Graph[node].duration=duration[node];
    Graph[node].EF=Graph[node].ES+Graph[node].duration;

    for(int i=0;i<adj[node].size();i++){
        int child_node = adj[node][i];
        Graph[child_node].ES = max(Graph[child_node].ES, Graph[node].EF);
        Graph[node].duration=duration[node];
    }
}

int main(){
    freopen("input.txt","r",stdin);

    string s;
    int index=0;
    char graph[200][200];

    while(cin>>s){
        cout<<s<<endl;

        string num_str;
        int type=0;
        char st[s.size()+10];
        int j=0;
        graph[index][j++]=s[0];

        for(int i=1;i<s.size();i++){
            if(s[i]>='0' and s[i]<='9'){
                num_str+=s[i];
            }
            if(s[i]>='A' and s[i]<='Z'){
                graph[index][j++]=s[i];
                type=2;
            }
        }
        // make graph
        for(int i=1;i<j;i++){
            //printf("%c",graph[index][i]);
            adj[graph[index][0]-'A'].push_back(graph[index][i]-'A');
        }
        int num = stoi(num_str);
        duration[index]=num;

        cout<<endl;
        cout<<num_str<<endl;
        index++;
    }
    for(int i=0;i<index;i++){
        printf("%c-->",i+'A');
        for(int j=0;j<adj[i].size();j++){
            printf("%c ",adj[i][j]+'A');
        }
        printf("\n");
    }
    

}