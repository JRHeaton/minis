#include <stdio.h>

extern void AMDeviceNotificationSubscribe(void (*cb)(void *), int, int, int, void **);
extern void AMDeviceConnect(void *);
extern void AMDevice