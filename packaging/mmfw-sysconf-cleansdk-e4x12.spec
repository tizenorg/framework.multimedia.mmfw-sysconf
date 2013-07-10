Name:       mmfw-sysconf-cleansdk-e4x12
Summary:    Multimedia Framework system configuration package
Version:    0.1.70
Release:    0
Group:      TO_BE/FILLED_IN
License:    Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz
ExclusiveArch:  %arm

%description
Multimedia Framework system configuration package

%prep
%setup -q -n mmfw-sysconf-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr
cp -arf mmfw-sysconf-cleansdk-e4x12/* %{buildroot}

%post 

%postun 

%files
%manifest mmfw-sysconf-cleansdk-e4x12.manifest
%defattr(-,root,root,-)
/etc/asound.conf
/etc/pulse/*
/usr/etc/*.ini
/usr/etc/gst-openmax.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/usr/share/pulseaudio/alsa-mixer/paths/*.common
/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
