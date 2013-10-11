# revision 29349
# category Package
# catalog-ctan /language/mongolian/montex
# catalog-date 2012-07-07 22:27:26 +0200
# catalog-license gpl
# catalog-version IVu.04.092
Name:		texlive-montex
Version:	IVu.04.092
Release:	3
Summary:	Mongolian LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/mongolian/montex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/montex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/montex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-cbfonts

%description
MonTeX provides Mongolian and Manju support for the TeX/LaTeX
community. Mongolian is a language spoken in North East Asia,
namely Mongolia and the Inner Mongol Autonomous Region of
China. Today, it is written in an extended Cyrillic alphabet in
Mongolia whereas the Uighur writing continues to be in use in
Inner Mongolia, though it is also, legally speaking, the
official writing system of Mongolia. Manju is another language
of North East Asia, belonging to the Tungusic branch of the
Altaic languages. Though it is hardly spoken nowadays, it
survives in written form as Manju was the native language of
the rulers of the Qing dynasty (1644-1911) in China. Large
quantities of documents of the Imperial Archives survive, as
well as some of the finest dictionaries ever compiled in Asia,
like the Pentaglot, a dictionary comprising Manju, Tibetan,
Mongolian, Uighur and Chinese. MonTeX provides all necessary
characters for writing standard Mongolian in Cyrillic and
Classical (aka Traditional or Uighur) writing, and Manju as
well as transliterated Tibetan texts, for which purpose a
number of additional characters was created. In MonTeX, both
Mongolian and Manju are entered in romanized form. The
retransliteration (from Latin input to Mongolian and Manju
output) is completely realized in TeX/Metafont so that no
external preprocessor is required. Please note that most of the
enhanced functions of MonTeX require a working e-LaTeX
environment. This is especially true when compiling documents
with Mongolian or Manju as the main document language. It is
recommended to choose pdfelatex as the resulting PDF files are
truly portable. Vertical text generated by MonTeX is not
supported in DVI.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/montex/mongolian.map
%{_texmfdistdir}/fonts/source/public/montex/bcghsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bcghsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bcghwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bcghwm.mf
%{_texmfdistdir}/fonts/source/public/montex/bcgvsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bcgvsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bcgvwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bcgvwm.mf
%{_texmfdistdir}/fonts/source/public/montex/bicighb.mf
%{_texmfdistdir}/fonts/source/public/montex/bicighm.mf
%{_texmfdistdir}/fonts/source/public/montex/bicigvb.mf
%{_texmfdistdir}/fonts/source/public/montex/bicigvm.mf
%{_texmfdistdir}/fonts/source/public/montex/bthhsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bthhsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bthhwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bthhwm.mf
%{_texmfdistdir}/fonts/source/public/montex/bthvsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bthvsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bthvwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bthvwm.mf
%{_texmfdistdir}/fonts/source/public/montex/bxghsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bxghsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bxghwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bxghwm.mf
%{_texmfdistdir}/fonts/source/public/montex/bxgvsb.mf
%{_texmfdistdir}/fonts/source/public/montex/bxgvsm.mf
%{_texmfdistdir}/fonts/source/public/montex/bxgvwb.mf
%{_texmfdistdir}/fonts/source/public/montex/bxgvwm.mf
%{_texmfdistdir}/fonts/source/public/montex/cyrmorec.mf
%{_texmfdistdir}/fonts/source/public/montex/cyrmorei.mf
%{_texmfdistdir}/fonts/source/public/montex/cyrmorel.mf
%{_texmfdistdir}/fonts/source/public/montex/cyrmoreu.mf
%{_texmfdistdir}/fonts/source/public/montex/kmb10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx5.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx6.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx7.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbx9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbxsl10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmbxti10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmcsc10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmcsc8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmcsc9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmdunh10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmff10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmfi10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmfib8.mf
%{_texmfdistdir}/fonts/source/public/montex/kminch.mf
%{_texmfdistdir}/fonts/source/public/montex/kmitt10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr17.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr5.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr6.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr7.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmr9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmsl10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmsl12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmsl8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmsl9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmsltt10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmss10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmss12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmss17.mf
%{_texmfdistdir}/fonts/source/public/montex/kmss8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmss9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssbx10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssdc10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssi10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssi12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssi17.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssi8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssi9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssq8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmssqi8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmtcsc10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmti10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmti12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmti7.mf
%{_texmfdistdir}/fonts/source/public/montex/kmti8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmti9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmtt10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmtt12.mf
%{_texmfdistdir}/fonts/source/public/montex/kmtt8.mf
%{_texmfdistdir}/fonts/source/public/montex/kmtt9.mf
%{_texmfdistdir}/fonts/source/public/montex/kmu10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmvtt10.mf
%{_texmfdistdir}/fonts/source/public/montex/kmvtti10.mf
%{_texmfdistdir}/fonts/source/public/montex/lmligs.mf
%{_texmfdistdir}/fonts/source/public/montex/macodes.mf
%{_texmfdistdir}/fonts/source/public/montex/maglyphs.mf
%{_texmfdistdir}/fonts/source/public/montex/mantrlig.mf
%{_texmfdistdir}/fonts/source/public/montex/mbatoms.mf
%{_texmfdistdir}/fonts/source/public/montex/mbcodes.mf
%{_texmfdistdir}/fonts/source/public/montex/mbglyphs.mf
%{_texmfdistdir}/fonts/source/public/montex/mbligtbl.mf
%{_texmfdistdir}/fonts/source/public/montex/mbnums.mf
%{_texmfdistdir}/fonts/source/public/montex/mbparmb.mf
%{_texmfdistdir}/fonts/source/public/montex/mbparmm.mf
%{_texmfdistdir}/fonts/source/public/montex/mbparms.mf
%{_texmfdistdir}/fonts/source/public/montex/mbpunc.mf
%{_texmfdistdir}/fonts/source/public/montex/mcccscco.mf
%{_texmfdistdir}/fonts/source/public/montex/mccoding.mf
%{_texmfdistdir}/fonts/source/public/montex/mctextit.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyccsc.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyitall.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyrill.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyrl.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyrligs.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyrsymb.mf
%{_texmfdistdir}/fonts/source/public/montex/mcyru.mf
%{_texmfdistdir}/fonts/source/public/montex/mcytitle.mf
%{_texmfdistdir}/fonts/source/public/montex/mlscodes.mf
%{_texmfdistdir}/fonts/source/public/montex/mocodes.mf
%{_texmfdistdir}/fonts/source/public/montex/moglyphs.mf
%{_texmfdistdir}/fonts/source/public/montex/montrlig.mf
%{_texmfdistdir}/fonts/source/public/montex/mxcodes.mf
%{_texmfdistdir}/fonts/source/public/montex/mxglyphs.mf
%{_texmfdistdir}/fonts/source/public/montex/mxntrlig.mf
%{_texmfdistdir}/fonts/tfm/public/montex/bcghsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcghsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcghwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcghwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcgvsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcgvsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcgvwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bcgvwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bicighb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bicighm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bicigvb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bicigvm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthhsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthhsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthhwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthhwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthvsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthvsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthvwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bthvwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxghsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxghsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxghwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxghwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxgvsb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxgvsm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxgvwb.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/bxgvwm.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmb10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmbxti10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmcsc8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmcsc9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmdunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmff10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmfi10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kminch.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmitt10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr17.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr5.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr6.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr7.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmr9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmss10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmss12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmss17.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmss8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmss9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmtcsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmti10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmti12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmti7.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmti8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmti9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmtt12.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmtt8.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmtt9.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmu10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmvtt10.tfm
%{_texmfdistdir}/fonts/tfm/public/montex/kmvtti10.tfm
%{_texmfdistdir}/fonts/type1/public/montex/bcghsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcghsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcghwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcghwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcgvsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcgvsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcgvwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bcgvwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bicighb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bicighm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bicigvb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bicigvm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthhsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthhsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthhwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthhwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthvsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthvsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthvwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bthvwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxghsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxghsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxghwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxghwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxgvsb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxgvsm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxgvwb.pfb
%{_texmfdistdir}/fonts/type1/public/montex/bxgvwm.pfb
%{_texmfdistdir}/fonts/type1/public/montex/kmbx10.pfb
%{_texmfdistdir}/fonts/type1/public/montex/kmr10.pfb
%{_texmfdistdir}/fonts/type1/public/montex/kmss10.pfb
%{_texmfdistdir}/tex/latex/montex/bicig.def
%{_texmfdistdir}/tex/latex/montex/bithe.def
%{_texmfdistdir}/tex/latex/montex/buryat.def
%{_texmfdistdir}/tex/latex/montex/cpctt.def
%{_texmfdistdir}/tex/latex/montex/cpdbk.def
%{_texmfdistdir}/tex/latex/montex/cpibmrus.def
%{_texmfdistdir}/tex/latex/montex/cpkoi.def
%{_texmfdistdir}/tex/latex/montex/cpmls.def
%{_texmfdistdir}/tex/latex/montex/cpmnk.def
%{_texmfdistdir}/tex/latex/montex/cpmos.def
%{_texmfdistdir}/tex/latex/montex/cpncc.def
%{_texmfdistdir}/tex/latex/montex/english.def
%{_texmfdistdir}/tex/latex/montex/kazakh.def
%{_texmfdistdir}/tex/latex/montex/lmabthhs.fd
%{_texmfdistdir}/tex/latex/montex/lmabthhw.fd
%{_texmfdistdir}/tex/latex/montex/lmabthvs.fd
%{_texmfdistdir}/tex/latex/montex/lmabthvw.fd
%{_texmfdistdir}/tex/latex/montex/lmaenc.def
%{_texmfdistdir}/tex/latex/montex/lmccmdh.fd
%{_texmfdistdir}/tex/latex/montex/lmccmfib.fd
%{_texmfdistdir}/tex/latex/montex/lmccmfr.fd
%{_texmfdistdir}/tex/latex/montex/lmccmiss.fd
%{_texmfdistdir}/tex/latex/montex/lmccmr.fd
%{_texmfdistdir}/tex/latex/montex/lmccmss.fd
%{_texmfdistdir}/tex/latex/montex/lmccmssq.fd
%{_texmfdistdir}/tex/latex/montex/lmccmtt.fd
%{_texmfdistdir}/tex/latex/montex/lmccmvtt.fd
%{_texmfdistdir}/tex/latex/montex/lmcenc.def
%{_texmfdistdir}/tex/latex/montex/lmclcmss.fd
%{_texmfdistdir}/tex/latex/montex/lmobcghs.fd
%{_texmfdistdir}/tex/latex/montex/lmobcghw.fd
%{_texmfdistdir}/tex/latex/montex/lmobcgvs.fd
%{_texmfdistdir}/tex/latex/montex/lmobcgvw.fd
%{_texmfdistdir}/tex/latex/montex/lmoenc.def
%{_texmfdistdir}/tex/latex/montex/lmsbcgh.fd
%{_texmfdistdir}/tex/latex/montex/lmsbcgv.fd
%{_texmfdistdir}/tex/latex/montex/lmsenc.def
%{_texmfdistdir}/tex/latex/montex/lmubxghs.fd
%{_texmfdistdir}/tex/latex/montex/lmubxghw.fd
%{_texmfdistdir}/tex/latex/montex/lmubxgvs.fd
%{_texmfdistdir}/tex/latex/montex/lmubxgvw.fd
%{_texmfdistdir}/tex/latex/montex/lmuenc.def
%{_texmfdistdir}/tex/latex/montex/mls.sty
%{_texmfdistdir}/tex/latex/montex/mlsgalig.tex
%{_texmfdistdir}/tex/latex/montex/mlstrans.tex
%{_texmfdistdir}/tex/latex/montex/mnhyphex.tex
%{_texmfdistdir}/tex/latex/montex/rlbicig.sty
%{_texmfdistdir}/tex/latex/montex/russian.def
%{_texmfdistdir}/tex/latex/montex/xalx.def
%doc %{_texmfdistdir}/doc/latex/montex/00README
%doc %{_texmfdistdir}/doc/latex/montex/00readme.mfinput.km
%doc %{_texmfdistdir}/doc/latex/montex/ANNOUNCE
%doc %{_texmfdistdir}/doc/latex/montex/EMTEX
%doc %{_texmfdistdir}/doc/latex/montex/HISTORY
%doc %{_texmfdistdir}/doc/latex/montex/INSTALL
%doc %{_texmfdistdir}/doc/latex/montex/MIKTEX
%doc %{_texmfdistdir}/doc/latex/montex/TODO
%doc %{_texmfdistdir}/doc/latex/montex/UPDATE
%doc %{_texmfdistdir}/doc/latex/montex/cyrename.pl
%doc %{_texmfdistdir}/doc/latex/montex/fontlist.tex
%doc %{_texmfdistdir}/doc/latex/montex/mfinput/bithe/testfont.input
%doc %{_texmfdistdir}/doc/latex/montex/mfinput/bithe/testfont.sh
%doc %{_texmfdistdir}/doc/latex/montex/mkmlsmf.pl
%doc %{_texmfdistdir}/doc/latex/montex/mls-diag.tex
%doc %{_texmfdistdir}/doc/latex/montex/mlsquick.pdf
%doc %{_texmfdistdir}/doc/latex/montex/mlsquick.tex
%doc %{_texmfdistdir}/doc/latex/montex/mnhyphen.tex
%doc %{_texmfdistdir}/doc/latex/montex/montex.pdf
%doc %{_texmfdistdir}/doc/latex/montex/montex.tex
%doc %{_texmfdistdir}/doc/latex/montex/montex.xml
%doc %{_texmfdistdir}/doc/latex/montex/mtdocmac.tex
%doc %{_texmfdistdir}/doc/latex/montex/testfont.input
%doc %{_texmfdistdir}/doc/latex/montex/testfont.sh
%doc %{_texmfdistdir}/doc/latex/montex/zanabazr.pdf
%doc %{_texmfdistdir}/doc/latex/montex/zanabazr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
