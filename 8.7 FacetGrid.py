mport seaborn as sns
import matplotlib.pyplot as plt
# Cargar el conjunto de datos 'penguins'
penguins = sns.load_dataset("penguins")
# Crear una cuadrícula de facetas segmentada por especie y sexo, con diferenciación por isla
g = sns.FacetGrid(penguins, col="species", row="sex", hue="island", height=3.5, aspect=1.2, margin_titles=True)
# Mapear un gráfico de dispersión de 'flipper_length_mm' vs 'body_mass_g' en la cuadrícula
g.map(sns.scatterplot, "flipper_length_mm", "body_mass_g", edgecolor="w")
# Añadir leyenda
g.add_legend(title="Isla de origen")
# Ajustar límites de los ejes
g.set(xlim=(170, 250), ylim=(2500, 6500))
# Añadir títulos y etiquetas
g.set_axis_labels("Largo de aleta (mm)", "Peso corporal (g)")
g.set_titles(col_template="Especie: {col_name}", row_template="Sexo: {row_name}")
# Ajustar espacio entre facetas
plt.subplots_adjust(hspace=0.4, wspace=0.4)
# Mostrar la visualización
plt.show()