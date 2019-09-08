import React, { Component } from 'react';
import './App.css';
import 'antd/dist/antd.css';
import { Input, Table } from 'antd'; //ant-design
import { Link, animateScroll as scroll } from "react-scroll"; //react-scroll
import dataSource from './dataSource'

const { Search } = Input;

class App extends Component {
  render(){

    const columns = [
      {
        title: 'Rank',
        dataIndex: 'rank',
        key: 'rank'
      },
      {
        title: 'Company Name',
        dataIndex: 'name',
        key: 'name'
      },
      {
        title: 'Score',
        dataIndex: 'score',
        key: 'score'
      },
      {
        title: 'FleschRE Score',
        dataIndex: 'fleschR',
        key: 'fleschR'
      },
      {
        title: 'Flesch-Kincaid Score',
        dataIndex: 'fleschK',
        key: 'fleschK'
      },
      {
        title: 'Average Sentence Length',
        dataIndex: 'ASL',
        key: 'ASL'
      },
    ]

    return (
      <div className="App">
        <main>
          <header className = "navbar">
          <h2> Privacy Policy Index </h2>
            <div className='alignRight'>
              <Link
                activeClass="active"
                to="stats"
                spy={true}
                smooth={true}
                offset={-78}
                duration={500}
              >
                Stats
              </Link>
              <Link
                activeClass="active"
                to="about"
                spy={true}
                smooth={true}
                offset={-30}
                duration={500}
              >
                About
              </Link>
              <Link
                activeClass="active"
                to="home"
                spy={true}
                smooth={true}
                offset={-78}
                duration={500}
              >
                Home
              </Link>
            </div>
          </header>

          <div className="body">
            <section className = "home-page" id = "home">
              <div className="middle-object">
                <h1> Enter A URL to Receive an Analysis of an Organization's Privacy Policy. </h1>
                <div className='center'>
                  <Search placeholder="Input URL" onSearch={value => console.log(value)} style={{marginBottom: '20px'}} enterButton/>
                  <Table dataSource={dataSource} columns={columns} pagination={{ pageSize: 7 }}/>
                </div>
              </div>
            </section>

            <section className = "about-page" id = "about">
              <div className = "left-half">
                <div className = "about-text">
                  <h1 className = "about-me">
                    ABOUT
                  </h1>
                  <hr className = "line"/>
                  <p className = "description">
                    The term "Privacy Paradox" describes the inconsistency between
                    our concerns about privacy and our seemingly apathetic behavior
                    towards giving information away. Oftentimes, corporations encourage
                    apathy with convoluted Privacy Policies that may hide content people
                    are likely to find concerning. The Privacy Policy Index (PPI) aims to
                    provide a <span style={{fontWeight: 'bold', color:'orange'}}>convenient</span> and <span style={{fontWeight: 'bold', color: 'yellow'}}>accessible</span>
                    {' '} starting point for looking into privacy policies. It uses Machine Learning <span style={{fontWeight: 'bold', color: 'lightGreen'}}>(Linear Regression)</span>
                    {' '} and several readability indexes to evaluate the strength of a company's
                    privacy policy and rank it against that of other companies.
                  </p>
                </div>
              </div>
            </section>

            <section className = "stats-page" id = "stats">
              <h1 className='text-center'> Data Collected </h1>
              <img src="Plot.png">
            </section>
          </div>
        </main>
      </div>
    );
  }
}

export default App;
