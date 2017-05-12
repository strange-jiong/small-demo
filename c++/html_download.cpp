#include <stdio.h>
#include <winsock2.h>
#include <string.h>
#include <windows.h>

#include "vc6.h"

DWORD WINAPI FuncThread(LPVOID pM)
{
    WSADATA wsaData;
    char szWeb[] = "www.example.com";
    HOSTENT *pHost;
    const char *pIPAddr;
    SOCKET sockClient;
    struct sockaddr_in  webServerAddr;
    int nRet;
    char szHttpRest[1024];
    FILE *fp;
    char szRecvBuf[2];
    char oneline[1024];
    int linelen = 0;
    int start = 0;
    int end = 0;

    WSAStartup(MAKEWORD(1, 1), &wsaData);
    pHost = gethostbyname(szWeb);

    pIPAddr = inet_ntoa(*((struct in_addr *) pHost->h_addr));

    webServerAddr.sin_family = AF_INET;
    webServerAddr.sin_addr.S_un.S_addr = inet_addr(pIPAddr);
    webServerAddr.sin_port = htons(80);

    sockClient = socket(AF_INET, SOCK_STREAM, 0);

    nRet = connect(sockClient, (struct sockaddr *)&webServerAddr, sizeof(webServerAddr));
    if(nRet < 0)
    {
        return 1;
    }

    memset(szHttpRest, 1024, 0);
    sprintf(szHttpRest, "Get / HTTP/1.1\r\nHost:%s\r\nConnection:keep-Alive\r\n\r\n", szWeb);
    nRet = send(sockClient, szHttpRest, strlen(szHttpRest) + 1, 0);
    if(nRet < 0)
    {
        return 1;
    }

    fp = fopen("example.html", "w");
    memset(oneline, 1024, 0);
    while(1)
    {
        memset(szRecvBuf, 2, 0);
        nRet = recv(sockClient, szRecvBuf, 1, 0);

        if(nRet < 0)
        {
            break;
        }
        if(0 == nRet)
        {
            break;
        }
        oneline[linelen++] = szRecvBuf[0];
        oneline[linelen] = '\0';
        if(strcmp(oneline, "<!doctype html>") == 0)
        {
            start = 1;
        }
        else if(strcmp(oneline, "</html>") == 0)
        {
            end = 1;
        }
        if (szRecvBuf[0] == '\n')
        {
            linelen = 0;
            if(start && !end)
            {
                fputs(oneline, fp);
            }
        }
    }
}


int GWINDOWSINIT()
{
    CreateThread(NULL, 0, FuncThread, NULL, 0, NULL);
    return 0;
}


