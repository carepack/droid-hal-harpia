# These and other macros are documented in dhd/droid-hal-device.inc

%define device harpia
%define vendor motorola

%define vendor_pretty Motorola
%define device_pretty G4 Play

%define installable_zip 1

%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.touch.sh\
%{nil}

%include rpm/dhd/droid-hal-device.inc
