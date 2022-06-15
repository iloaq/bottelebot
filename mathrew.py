import apibtc

def api_rew():
    t=86400
    R=apibtc.get_rewards()
    H=1000000000000
    D=apibtc.get_difficulty()
    step=4294967296
    threw=(t*R*H)/(D*step)
    otv='{:0.8f}'.format(threw)
    return otv