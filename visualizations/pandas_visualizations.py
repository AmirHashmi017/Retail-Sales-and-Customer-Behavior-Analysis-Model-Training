import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def generate_pandas_visualizations(df):
    visualizations = []
    
    # Visualization 1: Top 10 Items Purchased
    # Visualization 1: Top 10 Items Purchased
    plt.figure(figsize=(10, 6))
    
    # Get items frequency and prepare data for plotting
    item_counts = df['Item Purchased'].value_counts()
    top_10_items = item_counts.head(10)
    sorted_top_items = top_10_items.sort_values()
    
    # Create horizontal bar chart
    sorted_top_items.plot(kind='barh', color='teal')
    
    # Add chart labels
    plt.title('Top 10 Most Purchased Items')
    plt.xlabel('Count')
    plt.ylabel('Item')
    
    # Save and close
    visualizations.append(save_plot_to_base64(plt, 'Top 10 Items Purchased'))
    plt.close()
    # Visualization 2: Subscription Status Distribution
    plt.figure(figsize=(8, 6))
    # Get subscription status counts
    subscription_counts = df['Subscription Status'].value_counts()
    # Create pie chart
    subscription_counts.plot(
        kind='pie', 
        autopct='%1.1f%%', 
        colors=['lightcoral', 'lightgreen']
    )
    # Customize chart appearance
    plt.title('Subscription Status Distribution')
    plt.ylabel('')  # Remove y-label for cleaner look
    
    # Save and close
    visualizations.append(save_plot_to_base64(plt, 'Subscription Status Distribution'))
    plt.close()
    
    
    # Visualization 3: Previous Purchases Distribution    
    # Step 1: Create a new figure with specified size 
    plt.figure(figsize=(10, 6))
    purchase_history = df['Previous Purchases'] 
    purchase_history.plot(
        kind='hist',       # Create a histogram
        bins=20,           # Divide data into 20 bins
        edgecolor='black', # Add black edges to bars
        color='purple',    # Fill bars with purple color
        alpha=0.7          # Make bars slightly transparent (0.7 = 70% opaque)
    )
    plt.title('Distribution of Previous Purchases')
    plt.xlabel('Number of Previous Purchases')
    plt.ylabel('Count')
    
    # Step 4: Save the visualization and close the figure
    visualizations.append(save_plot_to_base64(plt, 'Previous Purchases Distribution'))
    plt.close()
    
    # Visualization 4: Purchase Amount Over Age
    plt.figure(figsize=(10, 6))
    df.plot(kind='scatter'
            , x='Age',
            y='Purchase Amount (USD)',
            alpha=0.5,
            color='orange')
    plt.title('Purchase Amount Over Age')
    plt.xlabel('Age')
    plt.ylabel('Purchase Amount (USD)')
    visualizations.append(save_plot_to_base64(plt, 'Purchase Amount Over Age'))
    plt.close()

    # Visualization 5: Payment Method Popularity
    plt.figure(figsize=(10, 6))
    payment_counts = df['Payment Method'].value_counts().sort_values()
    payment_counts.plot(
        kind='barh',
        color=['skyblue', 'lightgreen', 'salmon', 'gold'],
        edgecolor='black'
    )
    plt.title('Most Popular Payment Methods')
    plt.xlabel('Number of Transactions')
    plt.ylabel('Payment Method')
    plt.grid(axis='x', linestyle='--', alpha=0.4)
    visualizations.append(save_plot_to_base64(plt, 'Payment Method Popularity'))
    plt.close()

    # Visualization 6: Purchase Amount by Category
    plt.figure(figsize=(12, 6))
    df.boxplot(
        column='Purchase Amount (USD)',
        by='Category',
        vert=False,
        patch_artist=True,
        boxprops={'facecolor': 'lightblue'},
        flierprops={'marker': 'o', 'markersize': 5, 'markerfacecolor': 'red'}
    )
    plt.title('Purchase Amount Distribution by Category')
    plt.suptitle('')  
    plt.xlabel('Purchase Amount (USD)')
    plt.ylabel('Category')
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    visualizations.append(save_plot_to_base64(plt, 'Purchase Amount by Category'))
    plt.close()
    
    return {
        'library': 'pandas',
        'visualizations': visualizations
    }

def save_plot_to_base64(plt, title):
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    return {
        'title': title,
        'image': f'data:image/png;base64,{image_base64}'
    }