import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import calendar

# Carregue o DataFrame
df = pd.read_csv('Vendas.csv')

# a data tem que estar no formato Datetime
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

# Mapeando nome do mês para número do mês
month_to_num = {month: index for index, month in enumerate(calendar.month_name) if month}

df['Month'] = df['Data'].dt.strftime('%B')

df['MonthNum'] = df['Month'].map(month_to_num)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Função para criar um cartão de estatísticas com estilos
def create_card(card_id, title, background_color):
    card = dbc.Card(
        dbc.CardBody([
            html.H4(title, className="card-title", style={"text-align": "center"}),
            html.H5(id=card_id, className="card-text", style={"text-align": "center"}),
        ]),
        style={"background-color": background_color}
    )
    return card

# Layout do Dashboard
app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Vendas de Frutas"), width={'size': 12, 'offset': 3})),
    
    dbc.Row(dbc.Col(dcc.Dropdown(
        id='fruta-dropdown', clearable=False, value='Banana',
        options=[{'label': c, 'value': c} for c in df['Fruta'].unique()]
    ), width=4), justify='center'),
    
    dbc.Row([
        dbc.Col(create_card("total-sales", "Total", "#FFDDC1"), width=3),
        dbc.Col(create_card("average-sales", "Média", "#C1FFD7"), width=3),
        dbc.Col(create_card("min-sales", "Mínimo", "#C1D1FF"), width=3),
        dbc.Col(create_card("max-sales", "Máximo", "#FBC1FF"), width=3),
    ], className="mb-4"),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='scatter-plot'), width=6),
        dbc.Col(dcc.Graph(id='pie-chart'), width=6) 
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='sales-by-origin'), width=6),
        dbc.Col(dcc.Graph(id='boxplot'), width=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='stacked-bar-chart'), width=6),
        dbc.Col(dcc.Graph(id='area-chart'), width=6),  
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='heatmap'), width=6),
        dbc.Col(dcc.Graph(id='radar-chart'), width=6),
    ]),    
])

# Callbacks para atualizar os gráficos e cartões
@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('pie-chart', 'figure'), 
     Output('sales-by-origin', 'figure'),
     Output('boxplot', 'figure'),
     Output('stacked-bar-chart', 'figure'),
     Output('area-chart', 'figure'),
     Output('heatmap', 'figure'),
     Output('radar-chart', 'figure'),
     Output('total-sales', 'children'),
     Output('average-sales', 'children'),
     Output('min-sales', 'children'),
     Output('max-sales', 'children')],
    [Input('fruta-dropdown', 'value')]
)
def update_graphs_and_cards(selected_fruit):
    filtered_df = df[df['Fruta'] == selected_fruit]

    # Ordenar por MonthNum para garantir a ordem cronológica
    filtered_df = filtered_df.sort_values(by='MonthNum')

    # Atualizar gráfico de dispersão
    scatter_fig = px.scatter(filtered_df, x='MonthNum', y='Venda', color='Pais',
                             title=f'Vendas de {selected_fruit} por Mês')
    scatter_fig.update_xaxes(tickvals=list(range(1, 13)), ticktext=list(calendar.month_name)[1:])
    
    # Gráfico de torta
    pie_data = filtered_df.groupby('Month')['Venda'].sum().reset_index()
    pie_fig = px.pie(pie_data, values='Venda', names='Month', title=f'Distribuição de Vendas de {selected_fruit} por Mês')

    origin_fig = px.bar(filtered_df, x='Pais', y='Venda', title=f'Vendas de {selected_fruit} por País de Origem')
    boxplot_fig = px.box(filtered_df, y='Venda', title=f'Distribuição de Vendas de {selected_fruit}')

    # Gráfico de barras empilhadas para vendas por origem por mês
    stacked_fig = px.bar(filtered_df, x='Month', y='Venda', color='Pais',
                         title=f'Distribuição de Vendas de {selected_fruit} por Pais e Mês',
                         category_orders={"Month": list(calendar.month_name)[1:]})  # Garantindo a ordem dos meses

    # Calcular a soma das vendas por mês
    sum_sales = filtered_df.groupby('Month')['Venda'].sum().reset_index()
    # Mapear os nomes dos meses para números e ordenar
    sum_sales['MonthNum'] = sum_sales['Month'].map(month_to_num)
    sum_sales = sum_sales.sort_values(by='MonthNum')

    # Adicionar linha de média de vendas ao gráfico
    stacked_fig.add_scatter(x=sum_sales['Month'], y=sum_sales['Venda'], mode='lines', 
                            name='Vendas')

    # Gráfico de área para vendas acumuladas
    area_data = filtered_df.groupby('Data')['Venda'].sum().cumsum().reset_index()
    area_fig = px.area(area_data, x='Data', y='Venda', title='Vendas Acumuladas ao Longo do Tempo')
    
    # Gráfico de calor
    heatmap_data = df.pivot_table(values='Venda', index='Fruta', columns='Month', fill_value=0)
    heatmap_fig = px.imshow(heatmap_data, labels=dict(x="Mês", y="Fruta", color="Vendas"),
                            x=list(calendar.month_name)[1:], y=df['Fruta'].unique(),
                            title='Relação de Vendas por Fruta e Mês')
    
    # Preparação dos dados para o gráfico de radar
    radar_data = df.groupby('Fruta').agg({'Venda': ['sum', 'mean', 'max', 'min']}).reset_index()
    radar_data.columns = ['Fruta', 'Total Vendas', 'Média Vendas', 'Max Vendas', 'Min Vendas']
    
    # Gráfico de radar
    radar_fig = px.line_polar(radar_data, r='Total Vendas', theta='Fruta', line_close=True)
    radar_fig.update_traces(fill='toself')

    # (cálculo de estatísticas)
    total_sales = f"Total: {filtered_df['Venda'].sum():,.0f}"
    average_sales = f"Média: {filtered_df['Venda'].mean():.0f}"
    min_sales = f"Mínimo: {filtered_df['Venda'].min():.0f}"
    max_sales = f"Máximo: {filtered_df['Venda'].max():.0f}"

    return scatter_fig, pie_fig, origin_fig, boxplot_fig,  stacked_fig, area_fig, heatmap_fig, radar_fig, total_sales, average_sales, min_sales, max_sales

# Rodar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
