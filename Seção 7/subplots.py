import matplotlib.pyplot as plt

""" # Cria uma figura e uma grade de subplots
fig, axs = plt.subplots(nrows=1, ncols=2)

# Adicionando dados ao subplot esquerdo
axs[0].plot([1,2,3,4,5],[1,3,4,2,5], linewidth=2, color='#502299', label='esquerda')
axs[0].set_title('Subplot do lado esquerdo')

# Adicionando dados ao subplot direito
axs[1].barh(['A','B','C','D'], [8,15,6,7], color='orange')
axs[1].set_title('Subplot do lado direito')

axs[0].legend() """

# Conversão de polegada -> centímetro
cm = 1/2.54

fig, axs = plt.subplots(2,2, figsize=(28*cm, 20*cm), gridspec_kw={'width_ratios':[1.25,1]})

# Subplots
# Adicionando dados ao subplot superior esquerdo
axs[0,0].plot([1,2,3,4,5],[1,3,4,2,5], linewidth=2, color='#502299', label='esquerda')
axs[0,0].set_title('Subplot do lado superior esquerdo')

# Adicionando dados ao subplot superior direito
axs[0,1].barh(['A','B','C','D'], [8,15,6,7], color='orange')
axs[0,1].set_title('Subplot do lado superior direito')

# Adicionando dados ao subplot inferior esquerdo
axs[1,0].bar(['A','B','C','D'], [8,15,6,7], color='green')
axs[1,0].set_title('Subplot do lado inferior esquerdo')

# Adicionando dados ao subplot inferior direito
axs[1,1].pie([30,20,40], labels=['A','B','C'])
axs[1,1].set_title('Subplot do lado inferior direito')

fig.suptitle('Aula de subplot - Matplotlib')
fig.tight_layout(pad=2)

plt.show()