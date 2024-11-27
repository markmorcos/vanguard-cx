import streamlit as st
import matplotlib.pyplot as plt

from backend import Backend

def render_header():
    st.title("Vanguard Dashboard")

def render_demographics(be: Backend):
    st.subheader("Demographics")
    
    code, result = be.demo_age_group()
    st.write("#### Age Groups")
    with st.expander("##### Code"): st.code(code, language="sql")
    st.write("##### Result")
    st.table(result)

    code, result = be.demo_tenure()
    st.write("#### Tenure Groups")
    with st.expander("##### Code"): st.code(code, language="sql")
    st.write("##### Result")
    st.table(result)

def render_latest_visits_view(be: Backend):
    st.write("#### View: `latest_visits`")
    code = be.latest_visits()
    with st.expander("##### Code", expanded=True): st.code(code, language="sql")

def render_completion_rate(be: Backend):
    st.subheader("Completion Rate")

    code, result = be.completion_rate()
    with st.expander("##### Code"): st.code(code, language="sql")
    st.write("##### Result")
    st.table(result)
    
def render_step_completion_rate(be: Backend):
    st.subheader("Step Completion Rate")

    code, result = be.step_completion_rate()
    with st.expander("##### Code"): st.code(code, language="sql")
    st.write("##### Result")
    st.table(result)

    st.write("##### Plot")
    be.plot_step_completion_rate(test=False)
    be.plot_step_completion_rate(test=True)

def render_error_rate(be: Backend):
    st.subheader("Error Rate")

    code, result = be.error_rate_percentage()
    with st.expander("##### Code"): st.code(code, language="sql")
    st.write("##### Result")
    st.table(result)

def render_average_step_duration(be: Backend):
    st.subheader("Average Step Duration")

    code, result = be.average_step_duration()
   
    with st.expander("##### Code"): st.code(code, language="sql")
    
    st.write("##### Result")
    st.table(result)

    st.write("##### Plot")
    be.plot_step_average_time(test=False)
    be.plot_step_average_time(test=True)

def render_visit_kpis(be: Backend):
    st.subheader("KPIs")

    render_latest_visits_view(be)
    render_completion_rate(be)
    render_error_rate(be)
    render_step_completion_rate(be)
    render_average_step_duration(be)

def main():
    be = Backend()

    render_header()
    render_demographics(be)
    render_visit_kpis(be)

if __name__ == '__main__':
    main()
