tutorial%: tutorial%.cc
	g++ -I${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/include $@.cc -o $@ -lpythia8 -L${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/lib

tutorial3: tutorial3.cc
	g++ -I${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/include `root-config --cflags` $@.cc -o $@ -lpythia8 -L${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/lib `root-config --glibs`
	
tutorial4: tutorial4.cc
	g++ -I${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/include `root-config --cflags` $@.cc -o $@ -lpythia8 -L${HOME}/Desktop/UCM/Lessons/Fisica_De_Particulas/Pythia/pythia8313/lib `root-config --glibs`
	
