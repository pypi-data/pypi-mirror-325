# Implementation of Certified Training Methods

- [x] IBP (Gowal et al. , On the Effectiveness of Interval Bound Propagation for  Training Verifiably Robust Models, 2019)
- [x] Improved IBP (Shi et al., Fast Certified Robust Training with Short Warmup, 2021)
- [x] CROWN-IBP (Zhang et al., Towards Stable and Efficient Training of Verifably Robust Neural Networks)
- [x] SABR
- [x] TAPS
- [x] STAPS

TODO: Multiple Recent Papers by De Palma:
https://arxiv.org/pdf/2206.14772
https://arxiv.org/pdf/2305.13991
https://arxiv.org/pdf/2410.01617

## Setup
1. Create Virtual Environment and activate it
```
python3 -m venv ./venv
source venv/bin/activate
```
2. Clone auto_LiRPA

```
git clone git@github.com:Verified-Intelligence/auto_LiRPA.git
```
3. For complete verification, install $\alpha\beta$-CROWN

```
git clone git@github.com:Verified-Intelligence/alpha-beta-CROWN.git

```
Then, adjust the folder name and add an init file, s.t. we can import it as a module.
```
mv ./alpha-beta-CROWN ./abCROWN
touch ./abCROWN/__init__.py
```

4. Install Dependencies

On Linux:
```
pip3 install -r requirements_linux.txt
```
On MacOS:
```
pip3 install -r requirements_macos.txt
```
And install auto_LiRPA
```
pip3 install ./auto_LiRPA
```
## ToDos

- Investigate Crit. Eps for different certified training methods
- Investigate number of stable/unstable/active/inactive neurons