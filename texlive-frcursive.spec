# revision 17270
# category Package
# catalog-ctan /fonts/frcursive
# catalog-date 2010-02-28 22:13:22 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-frcursive
Version:	20100228
Release:	1
Summary:	French cursive hand fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/frcursive
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A hand-writing font in the style of the French academic
running-hand. The font is written in Metafont. An NFSS font
description and a supporting LaTeX package are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/frcursive/frca10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx17.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx7.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx8.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx9.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr17.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr7.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr8.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr9.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl17.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl7.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl8.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl9.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx11.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx12.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx17.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx7.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx8.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx9.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcursive.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcw10.mf
%{_texmfdistdir}/fonts/tfm/public/frcursive/frca10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr17.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr7.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr8.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr9.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl17.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl7.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx11.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx17.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcw10.tfm
%{_texmfdistdir}/metapost/frcursive/chars.mp
%{_texmfdistdir}/tex/latex/frcursive/frcursive.sty
%{_texmfdistdir}/tex/latex/frcursive/ot1frc.fd
%{_texmfdistdir}/tex/latex/frcursive/t1frc.fd
%doc %{_texmfdistdir}/doc/fonts/frcursive/COPYING
%doc %{_texmfdistdir}/doc/fonts/frcursive/FILES
%doc %{_texmfdistdir}/doc/fonts/frcursive/README
%doc %{_texmfdistdir}/doc/fonts/frcursive/doc/Makefile
%doc %{_texmfdistdir}/doc/fonts/frcursive/fcsource.tex
%doc %{_texmfdistdir}/doc/fonts/frcursive/figs.tex
%doc %{_texmfdistdir}/doc/fonts/frcursive/frcursive.pdf
%doc %{_texmfdistdir}/doc/fonts/frcursive/latex/Makefile
%doc %{_texmfdistdir}/doc/fonts/frcursive/lttst.tex
%doc %{_texmfdistdir}/doc/fonts/frcursive/mf/Makefile
%doc %{_texmfdistdir}/doc/fonts/frcursive/mkdrv.sh
%doc %{_texmfdistdir}/doc/fonts/frcursive/test/Makefile
%doc %{_texmfdistdir}/doc/fonts/frcursive/tfc.tex
%doc %{_texmfdistdir}/doc/fonts/frcursive/txt-en.tex
%doc %{_texmfdistdir}/doc/fonts/frcursive/txt-fr.tex
#- source
%doc %{_texmfdistdir}/source/fonts/frcursive/Makefile
%doc %{_texmfdistdir}/source/fonts/frcursive/frcursive.dtx
%doc %{_texmfdistdir}/source/fonts/frcursive/frcursive.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts metapost tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
