Name:       mmfw-sysconf
Summary:    Multimedia Framework system configuration package
Version:    0.1.260
Release:    0
VCS:        framework/multimedia/mmfw-sysconf#mmfw-sysconf_0.1.110-0-144-g25720f9f7daad9a897662eb6059d71d958cc3f06
Group:      System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0
Source0:    mmfw-sysconf-%{version}.tar.gz

%description
Multimedia Framework system configuration package

%ifarch %{arm}
%package cleansdk-e4x12
Summary: Multimedia Framework system configuration package for cleansdk-e4x12
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description cleansdk-e4x12
Multimedia Framework system configuration package for cleansdk-e4x12

%package e3250
Summary: Multimedia Framework system configuration package for e3250
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description e3250
Multimedia Framework system configuration package for e3250

%package hawkp
Summary: Multimedia Framework system configuration package for hawkp
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description hawkp
Multimedia Framework system configuration package for hawkp

%package sc7727s
Summary: Multimedia Framework system configuration package for sc7727s
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description sc7727s
Multimedia Framework system configuration package for sc7727s

%package sc7730s
Summary: Multimedia Framework system configuration package for sc7730s
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description sc7730s
Multimedia Framework system configuration package for sc7730s
%else
%package simulator
Summary: Multimedia Framework system configuration package for simulator
Group: System Environment/Multimedia
License:    LGPL-2.1+ and Apache-2.0

%description simulator
Multimedia Framework system configuration package for simulator
%endif

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/usr/share/license
%ifarch %{arm}
%if "%{?tizen_profile_name}" == "wearable"
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/%{name}-e3250
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/%{name}-e3250
%endif
%if "%{?tizen_profile_name}" == "mobile"
%if "%{?tizen_target_name}" == "Z130H"
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/%{name}-sc7727s
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/%{name}-sc7727s
%else
%if "%{?tizen_target_name}" == "Z300H"
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/%{name}-sc7730s
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/%{name}-sc7730s
%else
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/%{name}-cleansdk-e4x12
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/%{name}-cleansdk-e4x12
%endif
%endif
%endif
%if "%{?tizen_profile_name}" == "tv"
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/%{name}-hawkp
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/%{name}-hawkp
%endif
%else
cp LICENSE.APLv2.0 %{buildroot}/usr/share/license/mmfw-sysconf-simulator
cat LICENSE.LGPLv2.1 >> %{buildroot}/usr/share/license/mmfw-sysconf-simulator
%endif


%ifarch %{arm}
mkdir -p %{buildroot}/mmfw-sysconf-cleansdk-e4x12
cp -arf mmfw-sysconf-cleansdk-e4x12/* %{buildroot}/mmfw-sysconf-cleansdk-e4x12
mkdir -p %{buildroot}/mmfw-sysconf-e3250
cp -arf mmfw-sysconf-e3250/* %{buildroot}/mmfw-sysconf-e3250
mkdir -p %{buildroot}/mmfw-sysconf-hawkp
cp -arf mmfw-sysconf-hawkp/* %{buildroot}/mmfw-sysconf-hawkp
mkdir -p %{buildroot}/mmfw-sysconf-sc7727s
cp -arf mmfw-sysconf-sc7727s/* %{buildroot}/mmfw-sysconf-sc7727s
mkdir -p %{buildroot}/mmfw-sysconf-sc7730s
cp -arf mmfw-sysconf-sc7730s/* %{buildroot}/mmfw-sysconf-sc7730s
%else
mkdir -p %{buildroot}/mmfw-sysconf-simulator
cp -arf mmfw-sysconf-simulator/* %{buildroot}/mmfw-sysconf-simulator
%endif

%ifarch %{arm}
%post cleansdk-e4x12
cp -arf /mmfw-sysconf-cleansdk-e4x12/* /
rm -rf /mmfw-sysconf-cleansdk-e4x12
%post e3250
cp -arf /mmfw-sysconf-e3250/* /
rm -rf /mmfw-sysconf-e3250
%post hawkp
cp -arf /mmfw-sysconf-hawkp/* /
rm -rf /mmfw-sysconf-hawkp
%post sc7727s
cp -arf /mmfw-sysconf-sc7727s/* /
rm -rf /mmfw-sysconf-sc7727s
%post sc7730s
cp -arf /mmfw-sysconf-sc7730s/* /
rm -rf /mmfw-sysconf-sc7730s
%else
%post simulator
cp -arf /mmfw-sysconf-simulator/* /
rm -rf /mmfw-sysconf-simulator
%endif

%ifarch %{arm}
%files cleansdk-e4x12
%manifest mmfw-sysconf-cleansdk-e4x12.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-cleansdk-e4x12/etc/asound.conf
/mmfw-sysconf-cleansdk-e4x12/etc/pulse/*
/mmfw-sysconf-cleansdk-e4x12/usr/etc/*.ini
/mmfw-sysconf-cleansdk-e4x12/usr/etc/gst-openmax.conf
/mmfw-sysconf-cleansdk-e4x12/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-cleansdk-e4x12/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-cleansdk-e4x12/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/usr/share/license/*

%files e3250
%manifest mmfw-sysconf-e3250.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-e3250/etc/asound.conf
/mmfw-sysconf-e3250/etc/pulse/*
/mmfw-sysconf-e3250/etc/profile.d/*
/mmfw-sysconf-e3250/usr/etc/*.ini
/mmfw-sysconf-e3250/usr/etc/*.txt
/mmfw-sysconf-e3250/usr/etc/gst-openmax.conf
/mmfw-sysconf-e3250/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-e3250/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-e3250/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-e3250/opt/system/*
/usr/share/license/*

%files hawkp
%manifest mmfw-sysconf-hawkp.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-hawkp/etc/asound.conf
/mmfw-sysconf-hawkp/etc/pulse/*
/mmfw-sysconf-hawkp/usr/etc/*.ini
/mmfw-sysconf-hawkp/usr/etc/gstreamer-registry.sh
/mmfw-sysconf-hawkp/usr/etc/gstreamer-registry-copy.sh
/mmfw-sysconf-hawkp/usr/etc/gst-openmax.conf
/mmfw-sysconf-hawkp/usr/etc/gst-tz-openmax.conf
/mmfw-sysconf-hawkp/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-hawkp/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-hawkp/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/usr/share/license/*

%files sc7727s
%manifest mmfw-sysconf-sc7727s.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-sc7727s/etc/asound.conf
/mmfw-sysconf-sc7727s/etc/pulse/*
/mmfw-sysconf-sc7727s/etc/profile.d/*
/mmfw-sysconf-sc7727s/usr/etc/*.ini
/mmfw-sysconf-sc7727s/usr/etc/miccalib.txt
/mmfw-sysconf-sc7727s/usr/etc/codec_pga.xml
/mmfw-sysconf-sc7727s/usr/etc/audio_hw.xml
/mmfw-sysconf-sc7727s/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-sc7727s/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-sc7727s/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-sc7727s/opt/system/*
/usr/share/license/*

%files sc7730s
%manifest mmfw-sysconf-sc7730s.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-sc7730s/etc/asound.conf
/mmfw-sysconf-sc7730s/etc/pulse/*
/mmfw-sysconf-sc7730s/etc/profile.d/*
/mmfw-sysconf-sc7730s/usr/etc/*.ini
/mmfw-sysconf-sc7730s/usr/etc/miccalib.txt
/mmfw-sysconf-sc7730s/usr/etc/codec_pga.xml
/mmfw-sysconf-sc7730s/usr/etc/audio_hw.xml
/mmfw-sysconf-sc7730s/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-sc7730s/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-sc7730s/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/mmfw-sysconf-sc7730s/opt/system/*
/usr/share/license/*
%else
%files simulator
%manifest mmfw-sysconf-simulator.manifest
%defattr(-,root,root,-)
/mmfw-sysconf-simulator/etc/asound.conf
/mmfw-sysconf-simulator/etc/pulse/*
/mmfw-sysconf-simulator/usr/etc/*.ini
/mmfw-sysconf-simulator/usr/etc/gst-openmax.conf
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.conf
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/paths/*.common
/mmfw-sysconf-simulator/usr/share/pulseaudio/alsa-mixer/profile-sets/*.conf
/usr/share/license/mmfw-sysconf-simulator
%endif

