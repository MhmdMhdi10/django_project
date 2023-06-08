import {Link} from "react-router-dom"
import CartLoader from "../product/CartLoader";
import ProductCard from "../product/ProductCard";
import {useEffect, useState} from "react";

const products = [
    {
        id: 1,
        name: 'Black Basic Tee',
        price: '$32',
        href: '#',
        imageSrc: 'https://tailwindui.com/img/ecommerce-images/home-page-03-favorite-01.jpg',
        imageAlt: "Model wearing women's black cotton crewneck tee.",
    },
    // More products...
]

export default function ProductsSold({data}) {

    const [loading, setLoading] = useState(true)


    const sleep = ms => new Promise(
        resolve => setTimeout(resolve, ms)
    );

    useEffect(() => {
        async function fetchData() {
            setLoading(true)
            await sleep(3000);
            setLoading(false)
        }

        fetchData();
    }, [])
    return (
        <div className="bg-white">
            <div className="max-w-7xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:px-8">
                <div className="sm:flex sm:items-baseline sm:justify-between">
                    <h2 className="text-2xl font-extrabold tracking-tight text-gray-900">TOP</h2>
                </div>

                <div className="mt-6 grid grid-cols-1 gap-y-10 sm:grid-cols-3 sm:gap-y-0 sm:gap-x-6 lg:gap-x-8">
                    {data &&
                        data !== null &&
                        data !== undefined &&
                        data.map((product) => (
                            <>
                                {loading ? <CartLoader/> : <div key={product.id} className="group relative">
                                    <div
                                        className="shadow-xl w-full h-96 rounded-lg overflow-hidden group-hover:opacity-75 sm:h-auto sm:aspect-w-2 sm:aspect-h-3">
                                        <img
                                            src={product.photo}
                                            alt=""
                                            className="w-full h-full object-center object-cover"
                                        />
                                    </div>
                                    <h3 className="mt-4 text-base font-semibold text-gray-900">
                                        <Link to={`/product/${product.id}`}>
                                            <span className="absolute inset-0"/>
                                            {product.name}
                                        </Link>
                                    </h3>
                                    <p className="mt-1 text-sm text-gray-500">${product.price}</p>
                                </div>}
                            </>

                        ))}
                </div>

                <div className="mt-6 sm:hidden">
                    <Link to="#" className="block text-sm font-semibold text-indigo-600 hover:text-indigo-500">
                        Ver mas productos<span aria-hidden="true"> &rarr;</span>
                    </Link>
                </div>
            </div>
        </div>
    )
}
  