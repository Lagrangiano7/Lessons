#include <iostream>

#include "Pythia8/Pythia.h"

using namespace std;

int main(){

    int nevents = 10;
    Pythia8::Pythia pythia;

    pythia.readString("Beams:idA = 2212");
    pythia.readString("Beams:idB = 2212");
    pythia.readString("Beams:eCM = 14.e3");
    pythia.readString("SoftQCD:all = on");
    pythia.readString("HardQCD:all = on");

    Pythia8::Hist hpz("Momentum Distribution", 100, -10, 10);

    pythia.init();

    for (int i = 0; i < nevents; i++){
        if (!pythia.next()) continue;

        int entries = pythia.event.size();

        cout << "Event: " << i << endl;
        cout << "Event size: " << entries << endl;

        for (int j = 0; j < entries; j++){
            int id = pythia.event[j].id();
            double m = pythia.event[j].m();

            double px = pythia.event[j].px();
            double py = pythia.event[j].py();
            double pz = pythia.event[j].pz();

            double pabs = sqrt(pow(px, 2) + pow(py, 2) + pow(pz, 2));

            hpz.fill(pz); // Fill the histogram with the z component of momentums

            cout << id << " " << m << " " << pabs << endl;

        }

    }

    Pythia8::HistPlot hpl("tutorial2");
    hpl.frame("output", "Momentum Distribution", "Momentum", "Entries");
    hpl.add(hpz);
    hpl.plot();

    return 0;
}