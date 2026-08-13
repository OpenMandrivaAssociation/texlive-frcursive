%global tl_name frcursive
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	French cursive hand fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/frcursive
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
A hand-writing font in the style of the French academic running-hand.
The font was written in Metafont and has been converted to Adobe Type 1
format. LaTeX support (NFSS fd files, and a package) and font maps are
provided.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from frcursive:
Map frcursive.map
TL_DROPIN_EOF
