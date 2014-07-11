# revision 24559
# category Package
# catalog-ctan /fonts/frcursive
# catalog-date 2011-11-09 16:18:27 +0100
# catalog-license lppl1.2
# catalog-version undef
Name:		texlive-frcursive
Version:	20111109
Release:	8
Summary:	French cursive hand fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/frcursive
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A hand-writing font in the style of the French academic
running-hand. The font was written in Metafont and and has been
converted to Adobe Type 1 format. LaTeX support (NFFS fd files,
and a package) and font maps are provided.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/frcursive/frcursive.map
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcbx6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcc6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcf6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcr6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcsl6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslbx6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc10.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc14.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcslc6.mf
%{_texmfdistdir}/fonts/source/public/frcursive/frcursive.mf
%{_texmfdistdir}/fonts/tfm/public/frcursive/frca10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcc6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcf6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcr6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcsl6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc10.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc14.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcslc6.tfm
%{_texmfdistdir}/fonts/tfm/public/frcursive/frcw10.tfm
%{_texmfdistdir}/fonts/type1/public/frcursive/frca10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcbx10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcbx14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcbx6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcc10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcc14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcc6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcf10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcf14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcf6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcr10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcr14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcr6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcsl10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcsl14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcsl6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslbx6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslc10.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslc14.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcslc6.pfb
%{_texmfdistdir}/fonts/type1/public/frcursive/frcw10.pfb
%{_texmfdistdir}/tex/latex/frcursive/frcursive.sty
%{_texmfdistdir}/tex/latex/frcursive/ot1frc.fd
%{_texmfdistdir}/tex/latex/frcursive/t1frc.fd
%doc %{_texmfdistdir}/doc/fonts/frcursive/COPYING
%doc %{_texmfdistdir}/doc/fonts/frcursive/README
%doc %{_texmfdistdir}/doc/fonts/frcursive/frcursive.pdf
#- source

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111109-2
+ Revision: 752096
- Rebuild to reduce used resources

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111109-1
+ Revision: 732518
- Update to latest upstream version.

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100228-1
+ Revision: 718506
- texlive-frcursive
- texlive-frcursive
- texlive-frcursive
- texlive-frcursive

