# Actor-Critic with Experience Replay and and adaptation of action dispersion

Repozytorium oparte na zawiera implementację 
**Actor-Critic with Experience Replay and autocorrelated actions**, **Actor-Critic with Experience Replay** oraz **Actor-Critic with Experience Replay and and adaptation of action dispersion**.

## Instalacja

Wymagany Python3

1. Tworzenie wirtualnego środowiska
```shell script
python3.7 -m venv {name}
```

2. Aktywacja wirtualnego środowiska:
```shell script
source {name}/bin/activate 
```
3. Instalacja wymaganych bibliotek:
```shell script
pip install -r requirements.txt
``` 

4. Wywołanie programu:
```shell script
python run.py {args...}
``` 

## Przykładowe uruchomienia (wykorzystane do przeprowadzenia eksperymentów)

Algorytm ACER
```shell script
python acer/run.py --algo acer --env_name HalfCheetahBulletEnv-v0 \
    --gamma 0.95 --lam 0.9 --b 3 --c0 0.3 --c 10 --actor_lr 0.001 --critic_lr 0.002 \
    --actor_layers 20 --critic_layers 50 --memory_size 100000 --num_parallel_envs 10 \
    --actor_beta_penalty 0.1 --batches_per_env 10 --max_time_steps 1000000
```
Algprytm ACERAX
```shell script
python3.7 acer/run.py --algo acerax --env_name HalfCheetahBulletEnv-v0 \
    --gamma 0.95 --lam 0.9 --b 3 --c0 0.3 --c 10 --actor_lr 0.001 --critic_lr 0.002 \
    --actor_layers 20 --critic_layers 50 --memory_size 100000 --num_parallel_envs 10 \
    --actor_beta_penalty 0.1 --batches_per_env 10 --max_time_steps 1000000
```

Algorytm ACERAX ze zmienioną wielkością bufora memory_size
```shell script
python3.7 acer/run.py --algo acerax --env_name HalfCheetahBulletEnv-v0 \
    --gamma 0.95 --lam 0.9 --b 3 --c0 0.3 --c 10 --actor_lr 0.001 --critic_lr 0.002 \
    --actor_layers 20 --critic_layers 50 --memory_size 10000000 --num_parallel_envs 10 \
    --actor_beta_penalty 0.1 --batches_per_env 10 --max_time_steps 1000000
```

## References
Wawrzyński, Paweł.
"Reinforcement learning with experience replay and adaptation of action
dispersion"

Wawrzyński, Paweł.
*Real-time reinforcement learning by sequential actor–critics
and experience replay.*
Neural Networks 22.10 (2009): 1484-1497.

Wawrzyński, Paweł, and Ajay Kumar Tanwani.
*Autonomous reinforcement learning with experience replay.*
Neural Networks 41 (2013): 156-167.


