U
    P??a?%  ?                   @   s?   d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZe?d? dZddd?Zede? ?? dZd	Zd
d? Zdd? Ze?  dS )?    N?clearz?
  #####   #####  
 #     # #     # 
 #       #       
  #####  #  #### 
       # #     # 
 #     # #     # 
  #####   #####  
                 
?Bc                 C   s8   d}dD ]*}| |k r*| d?|? |? ?  S | | } qdS )zn
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    i   )? ?K?M?G?T?Pz.2fN? )?bytes?suffixZfactorZunitr
   r
   ?	SGLOAD.py?get_size   s
    r   z[31;1mZeth0?/root/dumpsc               	   C   sR  t ?d?} tdd?}|?? }|??  t?d? t ?d?}tdd?}t|?t| ? }|?? }|??  |??  t|?}t|?}|| }t?	? }t?
? }	t?? }
t?? }t?	? }t?? }t?? }
t?
? }	|d }t?d?}tj?? }t?? }t?? }t?? j}t?? }td|? d|? d	|? d
|? ?? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? tj?d? t|?dkr t|||? q d S )N?=grep eth0: /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'z'/sys/class/net/eth0/statistics/rx_bytes?r?   iH? ?/zMbps: z
PPS: z
CPU: z
 %
Cores: ?[1A?[2Ki'  )?
subprocess?	getoutput?open?read?close?time?sleep?int?psutilZvirtual_memoryZ	boot_timeZdisk_partitions?	cpu_countZswap_memoryZ
disk_usage?datetime?now?platform?uname?GPUtilZgetGPUsZcpu_freqZcurrent?cpu_percent?print?sys?stdout?write?dump)?Packets?
bytes1file?bytes1?Packets1?
bytes2file?pps?bytes2ZbbytesZsvmemZboot_time_timestampZ
partitionsZcoresZramZswap?mbpsZdiskr!   r#   ZgpusZ	frequency?cpur
   r
   r   ?main.   sn    







 r4   c           3      C   s?  d}g }g }g }|? t| ?? |? t|?? d}d}d}	d}
d}d}d}d}d}d}g }g }g }g }g }d}td| ? d|? d?? t?d?}t?dt? d	t? d
|? d?? tdt? d
|? d?? tt? d
|? d?d?}tj	?
|?}|D ?]?\}}tj?|?}|jtjjk?rq?|j}|j}|jtjjk?r?|j}|? t|j?? |d7 }|jtjj@ ?rb|? d? |jtjj@ ?r||? d? |jtjj@ ?r?|? d? |jtjjk?r?|j}d} |j}!|? t|!?? |d7 }|jtjjk?r?|	d7 }	|jtjjk?s|jtjjk?r|
d }
|?|j?j}"|? |"? t? |j!?}#|? t|#?? t? |j"?}$|? t|$?? |$|kr?|? |$? q?q?|D ]}|d7 }?qrt#||j$d?}%d|%k?r?d}d|%k?r?d}d|%k?r?d}|dk?rt#||j$d?}d|k?r?d}n$d|k?r?d}nd|k?rd}nd}t#||j$d?}!|!dk|%dk@ ?r.d}&?n2|!dk|%dk@ ?rHd}&?n|!dk|%dk@ ?rbd}&?n?|!dk|%dk@ ?r|d }&?n?|!d!k|%dk@ ?r?d"}&?n?|!d#k|%dk@ ?r?d$}&?n?|!d%k|%dk@ ?r?d&}&?n?|!d'k|%dk@ ?r?d(}&?n||!d)k|%dk@ ?r|&d*k ?n^|!d+k|%dk@ ?rd,}&?nD|!d-k|%dk@ ?r6d.}&?n*|!d/k|%dk@ ?rPd0}&?n|!d1k|%dk@ ?rhd2}&n?|!d3k|%dk@ ?r?d4}&n?|!d5k|%dk@ ?r?|&d6k n?|!d7k|%dk@ ?r?d8}&n?|!d9k|%dk@ ?r?d:}&n?|!d;k|%dk@ ?r?d<}&n||!d=k|%dk@ ?r?d>}&nd|!d?k|%dk@ ?rd@}&nL|!dAk|%dk@ ?r,dB}&n4|!dCk|%dk@ ?rDdD}&n|!dEk|%dk@ ?r\dF}&ndG}&t#||j$d?}#t#||j$d?}'t?d?}(tdH|(? dI?d?})g }*|D ],}||*k?r?|)?%|? dJ?? |*? |? n ?q?|)?&?  |dk?r(t?dKt? d
|? dL|? dM|? dM| ? dM|? dM|? dM|#? dM|'? dM|&? ?? nFt?dKt? d
|? dL|? dM|? dM| ? dM|? dM|? dM|#? dM|'? dM|&? ?? t?dN?}+tdOdP?},|,?'? }-|,?&?  t(?)d? t?dN?}.tdOdP?}/t|.?t|+? } |/?'? }0|,?&?  |/?&?  t|-?}-t|0?}0t*?+? }tdQ|? dR| ? dS|? dT|? ?? t,j-?%dU? t,j-?%dV? t,j-?%dU? t,j-?%dV? t,j-?%dU? t,j-?%dV? t,j-?%dU? t,j-?%dV? t,j-?%dU? t,j-?%dV? t,j-?%dU? t,j-?%dV? |d7 }dW| k?rntdX|? dY?? t#|?}1t#|?}2t.?  n ?qnd S )ZN?wr   ?sz
Attack Detected: z Packets Per Second | z Megabits Per Second
zdate +'%Y%m%d-%H%M'ztcpdump -i z -n -s0 -c 2000 -w z/dump.z.pcapzAttack Captured: ?rbr   ZSYNZACKZRSTZudp)?keyZTCP?UDPZICMPzTCP-SYNzTCP-ACKzTCP-RSTZ443ZKillallZ80Z37810ZDVRZ10001ZUbiquitiZ11211Z	MemcacheDZ1194zOpenVPN ReflectionZ137ZNetBIOSZ161ZSNMPZ1900ZSSDPZ30120ZFiveMZ30718zLantronix IOTZ32414zPlex Media ServerZ3283ZARDZ33848zJenkins Hudson AmplificationZ3389ZRDPZ3478ZSTUNZ3702ZWSDZ5351ZNATPMPZ53ZDNSZ5353ZMDNSZ123ZNTPZ5683ZCOAPZ8080Z	SpeedtestZUnknownr   z.txtz 
zpython3 sgload.py z.pcap ? r   z1/sys/devices/virtual/net/eth0/statistics/rx_bytesr   z$[35;1m[35mUnder Attack 
mbps: [35mz
[31mPackets Per Second: [35mz
[31mCPU Usage: [35m z%
[31mAttack Type: [35mr   r   i?  z
Last attack lasted z	 seconds
)/?appendr   r&   r   r   ?	interface?dump_directoryr   ?dpkt?pcap?ReaderZethernetZEthernet?typeZETH_TYPE_IP?data?p?ipZIP_PROTO_TCP?strZsport?flags?tcpZTH_SYNZTH_ACKZTH_RSTZIP_PROTO_UDPZIP_PROTO_ICMPZETH_TYPE_IP6Z	get_proto?__name__?socketZ	inet_ntoaZdst?src?max?countr)   r   r   r   r   r   r%   r'   r(   r4   )3r0   r2   r3   Zattack_type3Zpps_listZ	mbps_listZdest_ipsZ
tcpcounterZ
udpcounterZicmpcounterZ	ipcounterZattack_timerZ
syncounterZ
ackcounterZ	uniqueipsZ
rstcounterZcountersZipsZ	protocolsrF   Z
source_ipsZsource_portsZattack_type2?date?fr?   ZtsZbufZethrD   rG   r9   ZiptypeZsrcportrC   Zdst_ipZsrc_ipZattack_typeZvectorZMost_sourceZdate2?fileZniggers_testr+   r,   r-   r.   r/   r1   Zmax_ppsZmax_mbpsr
   r
   r   r*   i   sb   



 











HF




 
r*   )r   )r'   ?osr   r"   r   Zmathr$   r   r    Zrequestsr>   rI   ?system?asciir   r&   r<   r=   r4   r*   r
   r
   r
   r   ?<module>   s*   

; C