'use client'
import { link } from 'fs'
import Link from 'next/link'
import React from 'react'
import { AiFillBug } from 'react-icons/ai'
import { usePathname } from 'next/navigation'
import classnames from 'classnames'

const NavBar = () => {
    const pathname = usePathname()

    console.log(pathname)
    const links = [
        { href: '/', label: 'Dashboard' },
        { href: '/issues', label: 'Issues' },
    ]
    return (
        <nav className='flex space-x-6 border-b mb-5 px-5 h-14 items-center'>
            <Link href='/'>
                <AiFillBug />
            </Link>
            <ul className='flex space-x-6'>
                {links.map((link) => (
                    <Link
                        key={link.href}
                        // className={`${pathname === link.href ? 'text-zinc-900' : 'text-zinc-500'} hover:text-zinc-800 transition-colors`}
                        className={classnames({
                            'text-zinc-900': pathname === link.href,
                            'text-zinc-500': pathname !== link.href,
                            'hover:text-zinc-800 transition-colors': true
                        })}
                        href={link.href}
                    >{link.label}
                    </Link>
                ))}
            </ul>
        </nav>
    )
}

export default NavBar