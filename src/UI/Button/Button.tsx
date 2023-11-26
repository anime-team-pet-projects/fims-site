// import React from 'react'
import cls from 'classnames';
import style from "./Button.module.scss"
import { ReactNode } from 'react';
// import { Link } from 'react-router-dom';

interface ButtonProps {
    size?:'md' | 'sm' | 'xs',
    variant?:"primary"| "secondary",
    className?:string,
    children?:ReactNode,
    type?: "button"| "submit",
    disabled?: boolean,
}

export const Button = ({ 
        size="md",
        variant="primary", 
        className="",
        children,
        type= "button", 
        disabled=false
    }:ButtonProps) => {

    const classes = cls(
        className,
        style.btn,
        style[variant],
        style[size]
    );
    
    return <button type={type} className={classes} disabled={disabled}>{children}</button>
}