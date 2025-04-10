from preswald import text, plotly, connect, table, slider
import pandas as pd
import plotly.express as px

connect()

try:
    df = pd.read_csv('data/video games sales.csv')

    df.columns = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher',
                  'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

    text("# Video Game Sales Data 🎮")
    
    # Display the entire data (pagination automatic)
    text('### Raw Data')
    table(df)

    threshold = slider('Minimum Global Sales', min_val=0, max_val=100, default=20)

    filtered_df = df[df['Global_Sales'] > threshold]

    if not filtered_df.empty:
        text(f"### Games with Global Sales Greater than {threshold} Million")
        table(filtered_df)

        fig = px.scatter(
            filtered_df,
            x='NA_Sales',
            y='Global_Sales',
            color='Platform',
            size='Global_Sales',
            hover_name='Name',
            title='North America vs. Global Sales',
            labels={'NA_Sales': 'NA Sales (Millions)', 'Global_Sales': 'Global Sales (Millions)'}
        )

        fig.update_layout(template='plotly_white')
        plotly(fig)
    else:
        text("⚠️ No data matches your threshold.")

except Exception as e:
    text(f"❌ Error explicitly loading CSV: {str(e)}")

