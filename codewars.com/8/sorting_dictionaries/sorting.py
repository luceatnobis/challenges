#!/usr/bin/env python2.7

def sort_dict(d):
    return sorted(d.iteritems(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    sort_dict({3:1,2:2,1:3})
