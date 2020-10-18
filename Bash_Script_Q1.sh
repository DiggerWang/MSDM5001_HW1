#!/bin/bash

sysctl hw.l1icachesize
sysctl hw.l2cachesize
sysctl hw.l3cachesize
sysctl hw.memsize

df -hk
