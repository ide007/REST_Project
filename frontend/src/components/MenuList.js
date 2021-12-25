import React from 'react'
import {BrowserRouter, Link} from 'react-router-dom'

function Header () {
    return(
        <section>
            <header>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li><Link to='/users'> Участники </Link></li>
                            <li><Link to='/'> Проекты </Link></li>
                            <li><Link to='/taskboard'> Задачи </Link></li>
                            <li>
                                <form>
                                    <input type="string" />
                                    <button> Поиск </button>
                                </form>
                            </li>
                        </ul>
                        <hr/>
                    </nav>
                </BrowserRouter>
            </header>
        </section>
    )
}

export default Header
