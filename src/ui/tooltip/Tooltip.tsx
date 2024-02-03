import { ReactNode, useRef, useState, useEffect } from "react"
import {createPortal} from 'react-dom';
import style from "./tooltip.module.scss"
import cnBind from 'classnames/bind'
const cx = cnBind.bind(style)

interface PopoverProps {
    className?: string
    children?: ReactNode | string
    content?: ReactNode | string
    offset?: number    
    placement?: "top" | "bottom" | "right" | "left"
    trigger?: "hover" | "click" 
    teleportTarget?: HTMLElement
}

export const Tooltip = ({ 
        children,
        content, 
        teleportTarget = document.body,
        placement = "bottom",
        className = "",
        offset = 10,
        trigger = "hover", 
    }: PopoverProps) => {
    const [tooltipVisible, setTooltipVisible] = useState(false)
    const [positionArrow, setPositionArrow] = useState(placement)
    const triggerRef = useRef<HTMLDivElement>(null)
    const tooltipRef = useRef<HTMLDivElement>(null);

    const onClick = () => {
        setTooltipVisible(!tooltipVisible)
    }
    
    useEffect(() => {
        if (!tooltipVisible || !triggerRef.current || !tooltipRef.current) {
            return;
        }
        
        const triggerRect = triggerRef.current.getBoundingClientRect();
        const tooltipRect = tooltipRef.current.getBoundingClientRect();

        const location = {
            currentX: 0,
            currentY: 0,
            yTop: () => (triggerRect.top + window.scrollY) - tooltipRect.height - offset,
            yBottom: () =>  triggerRect.top + window.scrollY + triggerRect.height + offset,
            xLeft: () => triggerRect.x - tooltipRect.width - window.scrollX - offset,
            xRight: () => triggerRect.x + triggerRect.width + window.scrollX + offset,
            center() {
                if(placement === "top" || placement === "bottom") {
                    this.currentX = (triggerRect.x + window.scrollX + (triggerRect.width - tooltipRect.width) / 2)
                } else {
                    this.currentY = (triggerRect.bottom + window.scrollY - (triggerRect.height + tooltipRect.height) / 2)
                }
            },
            changeVertical(verticalLocation: () => number): void {
                this.center()
                this.currentY = verticalLocation()
            },
            changeHorizontal(horizontalLocation: () => number): void {
                this.center()
                this.currentX = horizontalLocation()
            }
        }
        
        switch (placement) {
            case "top":
                location.changeVertical(location.yTop)
                
                if(window.scrollY > location.currentY) {
                    location.changeVertical(location.yBottom)
                    setPositionArrow("bottom")
                    break
                } 

                setPositionArrow("top")
                break;

            case "bottom": {
                location.changeVertical(location.yBottom)

                const currentLocation = window.innerHeight - (location.currentY - window.scrollY + tooltipRect.height)

                if(currentLocation < 0) {
                    location.changeVertical(location.yTop)
                    setPositionArrow("top")
                    break
                } 

                setPositionArrow("bottom")
                break;
            }

            case "right":
                location.changeHorizontal(location.xRight)
                break;

            case "left":
                location.changeHorizontal(location.xLeft)
                break;
        }
        tooltipRef.current.style.transform = `translate(${location.currentX}px, ${location.currentY}px)`;
    }, [tooltipVisible, positionArrow, placement, offset]);
    const classes = cx(
        'tooltip__content',
        className,
    );

    return (
        <div className={cx("tooltip")}>
            {tooltipVisible && createPortal(
                <div 
                    className={classes}
                    ref={tooltipRef}
                >
                    <div className={cx("tooltip__arrow", positionArrow)}></div>

                    {content}
                </div>, 
                teleportTarget)
            } 
            
            <div 
                className="tooltip__trigger" 
                ref={triggerRef}
                onClick={() => trigger === "click" && onClick()}
                onMouseEnter={() => trigger === "hover" && setTooltipVisible(true)} 
                onMouseLeave={() => trigger === "hover" && setTooltipVisible(false)}
            >
                {children}

            </div>
        </div>
    )
}