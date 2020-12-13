# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv("/Users/philipp/Downloads/CSER-2020_Q3.csv")

### split dataframe for Facebook and Instagram data
df_fb = df[df['app'] == "Facebook"]
# new variables: appeal_ratio, restore_with_ratio, restore_without_ratio
    # probably you need a function that creates a new column with values for appeal_ration where existing and rest NAs
        # something like: if metric = content appealed,
# df_fb["appeal_ratio"] = np.where(df_fb['metric'] == "Content Appealed", df_fb['value']/df['value'].groupby("policyarea"))                             #df_fb["value"]/df_fb[]
df_insta = df[df['app'] == "Instagram"]
df_twitter = pd.read_csv("/Users/philipp/Downloads/Twitter_content moderation.csv")
df_youtube = pd.read_csv("/Users/philipp/Downloads/Youtube_videos removed.csv")

df_youtube_countries = pd.read_csv("/Users/philipp/Downloads/YouTube_country_data.csv")
# include Tabs to switch between platforms (or later between content types/ policy areas and have platform comparison in 1 Tab)

from dash.dependencies import Input, Output
##########
# building tabs with content as tab children (drawback that everything needs to be computed before, but I have a relatively small dataset so that should be okay)
#############
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']




##### FACEBOOK
fig_fb_actioned = px.bar(df_fb[df_fb['metric'] == "Content Actioned"], x="period", y="value", color="policy_area")  # , may be add barmode="group"
fig_fb_appealed = px.bar(df_fb[df_fb['metric'] == "Content Appealed"], x="period", y="value", color="policy_area")
fig_fb_restored_with = px.bar(df_fb[df_fb['metric'] == "Content Restored with appeal"], x="period", y="value", color="policy_area")
fig_fb_restored_without = px.bar(df_fb[df_fb['metric'] == "Content Restored without appeal"], x="period", y="value", color="policy_area")
fig_fb_proactive = px.bar(df_fb[df_fb['metric'] == "Proactive Rate"], x="period", y="value", color="policy_area", title= "Proactive rate of actioned content (in %)", barmode="group")
#fig_fb_proactive = px.line(df_fb[df_fb['metric'] == "Proactive Rate"], x="period", y="value",color = "policy_area", title='Proactive rate of action by content type')


####### INSTA
fig_insta_actioned = px.bar(df_insta[df_insta['metric'] == "Content Actioned"], x="period", y="value", color="policy_area")  # , may be add barmode="group"
fig_insta_appealed = px.bar(df_insta[df_insta['metric'] == "Content Appealed"], x="period", y="value", color="policy_area")
fig_insta_restored_with = px.bar(df_insta[df_insta['metric'] == "Content Restored with appeal"], x="period", y="value", color="policy_area")
fig_insta_restored_without = px.bar(df_insta[df_insta['metric'] == "Content Restored without appeal"], x="period", y="value", color="policy_area")
fig_insta_proactive = px.bar(df_insta[df_insta['metric'] == "Proactive Rate"], x="period", y="value", color="policy_area", title= "Proactive rate of actioned content (in %)", barmode="group")
#fig_insta_proactive = px.line(df_insta[df_insta['metric'] == "Proactive Rate"], x="period", y="value",color = "policy_area", title='Proactive rate of action by content type')

####### TWITTER
fig_twitter_accounts_actioned = px.bar(df_twitter, x= "Time period start", y = "Accounts actioned", color = "Rule name") # barmode = "grouped"
fig_twitter_accounts_suspended = px.bar(df_twitter, x= "Time period start", y = "Accounts suspended", color = "Rule name")
fig_twitter_content_removed = px.bar(df_twitter, x= "Time period start", y = "Content removed", color = "Rule name")

###### YOUTUBE
fig_youtube = px.bar(df_insta, x="period", y="value", color="policy_area")

# df = px.data.gapminder()
#fig_youtube_map = px.scatter_geo(df_youtube_countries, locations="iso_alpha", color="continent",
 #                    hover_name="Country", size="Value",
 #                    animation_frame="Period",
 #                    projection="natural earth")
#fig.show()

app.layout = html.Div(children=[
    html.H1(children='"Transparency" Reporting on Community Guideline and Legal Enforcement by social platforms. Algorithmic moderation on the rise..'),

    html.Div(children='''
        Welcome to my web application that visualizes transparency reporting by social platform corporations. In recent years
        social platforms have significantly extended their efforts to detect and remove harmful content by using
        algorithmic content moderation systems (ACMS). These however, come as all algorithmic systems with their inherent
        biases and uncertainties, which may have adverse effects on democratic rights. Pragmatically seen, the application of
        these systems seems necessary with respect to the volume of data circulating on global social media platforms. Nevertheless,
        the application of ACMS needs to be more transparent and most social platform corporations have only recently begun
        to report about removed content in more detail. Thus, this project seeks to provide a monitoring tool to compare
        developments between different platforms, which may otherwise be too time consuming for individual academics, journalists
        or any other interested person or organisation.

        *Click on categories to remove from graph and explore smaller categories, the scale will automatically adjust.
        E.g. for Facebook "Spam" and "Fake Accounts" are much more frequent than other types of illicit content or behaviour.
        Have fun exploring! 
    '''),

    html.Div(id='dd-output-container'),
        dcc.Tabs([
            dcc.Tab(label='Content Actioned', children=[
            dcc.Graph(
                figure= fig_fb_actioned
            )]),
            dcc.Tab(label='Content Appealed', children=[
            dcc.Graph(
                figure=fig_fb_appealed,
            )]),
            dcc.Tab(label='Content restored with Appeal', children=[
            dcc.Graph(
                figure= fig_fb_restored_with,
            )]),
            dcc.Tab(label='Content restored without Appeal', children=[
            dcc.Graph(
                figure= fig_fb_restored_without,
            )]),
            dcc.Tab(label='Proactive Rate', children=[
            dcc.Graph(
                figure= fig_fb_proactive,
            )]),

    ]),

# New Div for all elements in the new 'row' of the page

    html.H1(children=''),

        html.Div(children='''
            Instagram
        '''),
        dcc.Tabs([
            dcc.Tab(label='Content Actioned', children=[
            dcc.Graph(
                figure= fig_insta_actioned
            )]),
            dcc.Tab(label='Content Appealed', children=[
            dcc.Graph(
                figure=fig_insta_appealed,
            )]),
            dcc.Tab(label='Content restored with Appeal', children=[
            dcc.Graph(
                figure= fig_insta_restored_with,
            )]),
            dcc.Tab(label='Content restored without Appeal', children=[
            dcc.Graph(
                figure= fig_insta_restored_without,
            )]),
            dcc.Tab(label='Proactive Rate', children=[
            dcc.Graph(
                figure= fig_insta_proactive,
            )]),




    ]),

# New Div for all elements in the new 'row' of the page
html.Div([
        html.H1(children=''),

        html.Div(children='''
            Twitter
        '''),
        dcc.Tabs([
            dcc.Tab(label='Accounts Actioned', children=[
            dcc.Graph(
                figure= fig_twitter_accounts_actioned
            )]),
            dcc.Tab(label='Accounts suspended', children=[
            dcc.Graph(
                figure=fig_twitter_accounts_suspended,
            )]),
            dcc.Tab(label='Content removed', children=[
            dcc.Graph(
                figure= fig_twitter_content_removed
            )])]),




# New Div for all elements in the new 'row' of the page
html.Div([
        html.H1(children=''),

    html.Div(children='''
            Youtube - Videos removed
        '''),

        dcc.Graph(
            id='graph4',
            figure=fig_youtube
        ),
    ]),


#html.Div([
#        html.H1(children=''),

#        html.Div(children='''
#            Youtube - Videos removed per country
#        '''),

#        dcc.Graph(
#            id='graph5',
#            figure=fig_youtube_map
#        ),
#    ]),

])])


if __name__ == '__main__':
    app.run_server(debug=True)


