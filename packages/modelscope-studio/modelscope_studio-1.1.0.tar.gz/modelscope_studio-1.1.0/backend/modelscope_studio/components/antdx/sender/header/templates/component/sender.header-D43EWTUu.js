import { i as En, a as Ne, r as gn, g as hn, w as ce, c as le } from "./Index-B0J-JwSn.js";
const v = window.ms_globals.React, F = window.ms_globals.React, pn = window.ms_globals.React.forwardRef, K = window.ms_globals.React.useRef, vn = window.ms_globals.React.useState, ee = window.ms_globals.React.useEffect, mn = window.ms_globals.React.isValidElement, yn = window.ms_globals.React.useLayoutEffect, at = window.ms_globals.ReactDOM, je = window.ms_globals.ReactDOM.createPortal, bn = window.ms_globals.internalContext.useContextPropsContext, _n = window.ms_globals.antdIcons.CloseOutlined, Sn = window.ms_globals.antd.Button, wn = window.ms_globals.antd.ConfigProvider;
var Cn = /\s/;
function Rn(e) {
  for (var t = e.length; t-- && Cn.test(e.charAt(t)); )
    ;
  return t;
}
var Pn = /^\s+/;
function xn(e) {
  return e && e.slice(0, Rn(e) + 1).replace(Pn, "");
}
var st = NaN, Tn = /^[-+]0x[0-9a-f]+$/i, An = /^0b[01]+$/i, On = /^0o[0-7]+$/i, Ln = parseInt;
function ut(e) {
  if (typeof e == "number")
    return e;
  if (En(e))
    return st;
  if (Ne(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = Ne(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = xn(e);
  var n = An.test(e);
  return n || On.test(e) ? Ln(e.slice(2), n ? 2 : 8) : Tn.test(e) ? st : +e;
}
var Ae = function() {
  return gn.Date.now();
}, kn = "Expected a function", In = Math.max, jn = Math.min;
function Nn(e, t, n) {
  var r, o, i, a, s, l, c = 0, p = !1, u = !1, d = !0;
  if (typeof e != "function")
    throw new TypeError(kn);
  t = ut(t) || 0, Ne(n) && (p = !!n.leading, u = "maxWait" in n, i = u ? In(ut(n.maxWait) || 0, t) : i, d = "trailing" in n ? !!n.trailing : d);
  function f(m) {
    var C = r, L = o;
    return r = o = void 0, c = m, a = e.apply(L, C), a;
  }
  function _(m) {
    return c = m, s = setTimeout(S, t), p ? f(m) : a;
  }
  function y(m) {
    var C = m - l, L = m - c, Q = t - C;
    return u ? jn(Q, i - L) : Q;
  }
  function h(m) {
    var C = m - l, L = m - c;
    return l === void 0 || C >= t || C < 0 || u && L >= i;
  }
  function S() {
    var m = Ae();
    if (h(m))
      return P(m);
    s = setTimeout(S, y(m));
  }
  function P(m) {
    return s = void 0, d && r ? f(m) : (r = o = void 0, a);
  }
  function w() {
    s !== void 0 && clearTimeout(s), c = 0, r = l = o = s = void 0;
  }
  function E() {
    return s === void 0 ? a : P(Ae());
  }
  function x() {
    var m = Ae(), C = h(m);
    if (r = arguments, o = this, l = m, C) {
      if (s === void 0)
        return _(l);
      if (u)
        return clearTimeout(s), s = setTimeout(S, t), f(l);
    }
    return s === void 0 && (s = setTimeout(S, t)), a;
  }
  return x.cancel = w, x.flush = E, x;
}
var Ot = {
  exports: {}
}, ve = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Mn = F, $n = Symbol.for("react.element"), Dn = Symbol.for("react.fragment"), Fn = Object.prototype.hasOwnProperty, Un = Mn.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Vn = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function Lt(e, t, n) {
  var r, o = {}, i = null, a = null;
  n !== void 0 && (i = "" + n), t.key !== void 0 && (i = "" + t.key), t.ref !== void 0 && (a = t.ref);
  for (r in t) Fn.call(t, r) && !Vn.hasOwnProperty(r) && (o[r] = t[r]);
  if (e && e.defaultProps) for (r in t = e.defaultProps, t) o[r] === void 0 && (o[r] = t[r]);
  return {
    $$typeof: $n,
    type: e,
    key: i,
    ref: a,
    props: o,
    _owner: Un.current
  };
}
ve.Fragment = Dn;
ve.jsx = Lt;
ve.jsxs = Lt;
Ot.exports = ve;
var Oe = Ot.exports;
const {
  SvelteComponent: Kn,
  assign: ct,
  binding_callbacks: lt,
  check_outros: Wn,
  children: kt,
  claim_element: It,
  claim_space: Hn,
  component_subscribe: ft,
  compute_slots: zn,
  create_slot: Bn,
  detach: Y,
  element: jt,
  empty: dt,
  exclude_internal_props: pt,
  get_all_dirty_from_scope: Qn,
  get_slot_changes: Gn,
  group_outros: qn,
  init: Yn,
  insert_hydration: fe,
  safe_not_equal: Jn,
  set_custom_element_data: Nt,
  space: Xn,
  transition_in: de,
  transition_out: Me,
  update_slot_base: Zn
} = window.__gradio__svelte__internal, {
  beforeUpdate: er,
  getContext: tr,
  onDestroy: nr,
  setContext: rr
} = window.__gradio__svelte__internal;
function vt(e) {
  let t, n;
  const r = (
    /*#slots*/
    e[7].default
  ), o = Bn(
    r,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = jt("svelte-slot"), o && o.c(), this.h();
    },
    l(i) {
      t = It(i, "SVELTE-SLOT", {
        class: !0
      });
      var a = kt(t);
      o && o.l(a), a.forEach(Y), this.h();
    },
    h() {
      Nt(t, "class", "svelte-1rt0kpf");
    },
    m(i, a) {
      fe(i, t, a), o && o.m(t, null), e[9](t), n = !0;
    },
    p(i, a) {
      o && o.p && (!n || a & /*$$scope*/
      64) && Zn(
        o,
        r,
        i,
        /*$$scope*/
        i[6],
        n ? Gn(
          r,
          /*$$scope*/
          i[6],
          a,
          null
        ) : Qn(
          /*$$scope*/
          i[6]
        ),
        null
      );
    },
    i(i) {
      n || (de(o, i), n = !0);
    },
    o(i) {
      Me(o, i), n = !1;
    },
    d(i) {
      i && Y(t), o && o.d(i), e[9](null);
    }
  };
}
function or(e) {
  let t, n, r, o, i = (
    /*$$slots*/
    e[4].default && vt(e)
  );
  return {
    c() {
      t = jt("react-portal-target"), n = Xn(), i && i.c(), r = dt(), this.h();
    },
    l(a) {
      t = It(a, "REACT-PORTAL-TARGET", {
        class: !0
      }), kt(t).forEach(Y), n = Hn(a), i && i.l(a), r = dt(), this.h();
    },
    h() {
      Nt(t, "class", "svelte-1rt0kpf");
    },
    m(a, s) {
      fe(a, t, s), e[8](t), fe(a, n, s), i && i.m(a, s), fe(a, r, s), o = !0;
    },
    p(a, [s]) {
      /*$$slots*/
      a[4].default ? i ? (i.p(a, s), s & /*$$slots*/
      16 && de(i, 1)) : (i = vt(a), i.c(), de(i, 1), i.m(r.parentNode, r)) : i && (qn(), Me(i, 1, 1, () => {
        i = null;
      }), Wn());
    },
    i(a) {
      o || (de(i), o = !0);
    },
    o(a) {
      Me(i), o = !1;
    },
    d(a) {
      a && (Y(t), Y(n), Y(r)), e[8](null), i && i.d(a);
    }
  };
}
function mt(e) {
  const {
    svelteInit: t,
    ...n
  } = e;
  return n;
}
function ir(e, t, n) {
  let r, o, {
    $$slots: i = {},
    $$scope: a
  } = t;
  const s = zn(i);
  let {
    svelteInit: l
  } = t;
  const c = ce(mt(t)), p = ce();
  ft(e, p, (E) => n(0, r = E));
  const u = ce();
  ft(e, u, (E) => n(1, o = E));
  const d = [], f = tr("$$ms-gr-react-wrapper"), {
    slotKey: _,
    slotIndex: y,
    subSlotIndex: h
  } = hn() || {}, S = l({
    parent: f,
    props: c,
    target: p,
    slot: u,
    slotKey: _,
    slotIndex: y,
    subSlotIndex: h,
    onDestroy(E) {
      d.push(E);
    }
  });
  rr("$$ms-gr-react-wrapper", S), er(() => {
    c.set(mt(t));
  }), nr(() => {
    d.forEach((E) => E());
  });
  function P(E) {
    lt[E ? "unshift" : "push"](() => {
      r = E, p.set(r);
    });
  }
  function w(E) {
    lt[E ? "unshift" : "push"](() => {
      o = E, u.set(o);
    });
  }
  return e.$$set = (E) => {
    n(17, t = ct(ct({}, t), pt(E))), "svelteInit" in E && n(5, l = E.svelteInit), "$$scope" in E && n(6, a = E.$$scope);
  }, t = pt(t), [r, o, p, u, s, l, a, i, P, w];
}
class ar extends Kn {
  constructor(t) {
    super(), Yn(this, t, ir, or, Jn, {
      svelteInit: 5
    });
  }
}
const yt = window.ms_globals.rerender, Le = window.ms_globals.tree;
function sr(e, t = {}) {
  function n(r) {
    const o = ce(), i = new ar({
      ...r,
      props: {
        svelteInit(a) {
          window.ms_globals.autokey += 1;
          const s = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: e,
            props: a.props,
            slot: a.slot,
            target: a.target,
            slotIndex: a.slotIndex,
            subSlotIndex: a.subSlotIndex,
            ignore: t.ignore,
            slotKey: a.slotKey,
            nodes: []
          }, l = a.parent ?? Le;
          return l.nodes = [...l.nodes, s], yt({
            createPortal: je,
            node: Le
          }), a.onDestroy(() => {
            l.nodes = l.nodes.filter((c) => c.svelteInstance !== o), yt({
              createPortal: je,
              node: Le
            });
          }), s;
        },
        ...r.props
      }
    });
    return o.set(i), i;
  }
  return new Promise((r) => {
    window.ms_globals.initializePromise.then(() => {
      r(n);
    });
  });
}
const ur = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function cr(e) {
  return e ? Object.keys(e).reduce((t, n) => {
    const r = e[n];
    return t[n] = lr(n, r), t;
  }, {}) : {};
}
function lr(e, t) {
  return typeof t == "number" && !ur.includes(e) ? t + "px" : t;
}
function $e(e) {
  const t = [], n = e.cloneNode(!1);
  if (e._reactElement) {
    const o = F.Children.toArray(e._reactElement.props.children).map((i) => {
      if (F.isValidElement(i) && i.props.__slot__) {
        const {
          portals: a,
          clonedElement: s
        } = $e(i.props.el);
        return F.cloneElement(i, {
          ...i.props,
          el: s,
          children: [...F.Children.toArray(i.props.children), ...a]
        });
      }
      return null;
    });
    return o.originalChildren = e._reactElement.props.children, t.push(je(F.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: o
    }), n)), {
      clonedElement: n,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((o) => {
    e.getEventListeners(o).forEach(({
      listener: a,
      type: s,
      useCapture: l
    }) => {
      n.addEventListener(s, a, l);
    });
  });
  const r = Array.from(e.childNodes);
  for (let o = 0; o < r.length; o++) {
    const i = r[o];
    if (i.nodeType === 1) {
      const {
        clonedElement: a,
        portals: s
      } = $e(i);
      t.push(...s), n.appendChild(a);
    } else i.nodeType === 3 && n.appendChild(i.cloneNode());
  }
  return {
    clonedElement: n,
    portals: t
  };
}
function fr(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const dr = pn(({
  slot: e,
  clone: t,
  className: n,
  style: r,
  observeAttributes: o
}, i) => {
  const a = K(), [s, l] = vn([]), {
    forceClone: c
  } = bn(), p = c ? !0 : t;
  return ee(() => {
    var _;
    if (!a.current || !e)
      return;
    let u = e;
    function d() {
      let y = u;
      if (u.tagName.toLowerCase() === "svelte-slot" && u.children.length === 1 && u.children[0] && (y = u.children[0], y.tagName.toLowerCase() === "react-portal-target" && y.children[0] && (y = y.children[0])), fr(i, y), n && y.classList.add(...n.split(" ")), r) {
        const h = cr(r);
        Object.keys(h).forEach((S) => {
          y.style[S] = h[S];
        });
      }
    }
    let f = null;
    if (p && window.MutationObserver) {
      let y = function() {
        var w, E, x;
        (w = a.current) != null && w.contains(u) && ((E = a.current) == null || E.removeChild(u));
        const {
          portals: S,
          clonedElement: P
        } = $e(e);
        u = P, l(S), u.style.display = "contents", d(), (x = a.current) == null || x.appendChild(u);
      };
      y();
      const h = Nn(() => {
        y(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      f = new window.MutationObserver(h), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      u.style.display = "contents", d(), (_ = a.current) == null || _.appendChild(u);
    return () => {
      var y, h;
      u.style.display = "", (y = a.current) != null && y.contains(u) && ((h = a.current) == null || h.removeChild(u)), f == null || f.disconnect();
    };
  }, [e, p, n, r, i, o]), F.createElement("react-child", {
    ref: a,
    style: {
      display: "contents"
    }
  }, ...s);
});
function k(e) {
  "@babel/helpers - typeof";
  return k = typeof Symbol == "function" && typeof Symbol.iterator == "symbol" ? function(t) {
    return typeof t;
  } : function(t) {
    return t && typeof Symbol == "function" && t.constructor === Symbol && t !== Symbol.prototype ? "symbol" : typeof t;
  }, k(e);
}
function pr(e, t) {
  if (k(e) != "object" || !e) return e;
  var n = e[Symbol.toPrimitive];
  if (n !== void 0) {
    var r = n.call(e, t || "default");
    if (k(r) != "object") return r;
    throw new TypeError("@@toPrimitive must return a primitive value.");
  }
  return (t === "string" ? String : Number)(e);
}
function Mt(e) {
  var t = pr(e, "string");
  return k(t) == "symbol" ? t : t + "";
}
function T(e, t, n) {
  return (t = Mt(t)) in e ? Object.defineProperty(e, t, {
    value: n,
    enumerable: !0,
    configurable: !0,
    writable: !0
  }) : e[t] = n, e;
}
function Et(e, t) {
  var n = Object.keys(e);
  if (Object.getOwnPropertySymbols) {
    var r = Object.getOwnPropertySymbols(e);
    t && (r = r.filter(function(o) {
      return Object.getOwnPropertyDescriptor(e, o).enumerable;
    })), n.push.apply(n, r);
  }
  return n;
}
function b(e) {
  for (var t = 1; t < arguments.length; t++) {
    var n = arguments[t] != null ? arguments[t] : {};
    t % 2 ? Et(Object(n), !0).forEach(function(r) {
      T(e, r, n[r]);
    }) : Object.getOwnPropertyDescriptors ? Object.defineProperties(e, Object.getOwnPropertyDescriptors(n)) : Et(Object(n)).forEach(function(r) {
      Object.defineProperty(e, r, Object.getOwnPropertyDescriptor(n, r));
    });
  }
  return e;
}
function vr(e) {
  if (Array.isArray(e)) return e;
}
function mr(e, t) {
  var n = e == null ? null : typeof Symbol < "u" && e[Symbol.iterator] || e["@@iterator"];
  if (n != null) {
    var r, o, i, a, s = [], l = !0, c = !1;
    try {
      if (i = (n = n.call(e)).next, t === 0) {
        if (Object(n) !== n) return;
        l = !1;
      } else for (; !(l = (r = i.call(n)).done) && (s.push(r.value), s.length !== t); l = !0) ;
    } catch (p) {
      c = !0, o = p;
    } finally {
      try {
        if (!l && n.return != null && (a = n.return(), Object(a) !== a)) return;
      } finally {
        if (c) throw o;
      }
    }
    return s;
  }
}
function gt(e, t) {
  (t == null || t > e.length) && (t = e.length);
  for (var n = 0, r = Array(t); n < t; n++) r[n] = e[n];
  return r;
}
function yr(e, t) {
  if (e) {
    if (typeof e == "string") return gt(e, t);
    var n = {}.toString.call(e).slice(8, -1);
    return n === "Object" && e.constructor && (n = e.constructor.name), n === "Map" || n === "Set" ? Array.from(e) : n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? gt(e, t) : void 0;
  }
}
function Er() {
  throw new TypeError(`Invalid attempt to destructure non-iterable instance.
In order to be iterable, non-array objects must have a [Symbol.iterator]() method.`);
}
function D(e, t) {
  return vr(e) || mr(e, t) || yr(e, t) || Er();
}
function ht(e) {
  return e instanceof HTMLElement || e instanceof SVGElement;
}
function gr(e) {
  return e && k(e) === "object" && ht(e.nativeElement) ? e.nativeElement : ht(e) ? e : null;
}
function hr(e) {
  var t = gr(e);
  if (t)
    return t;
  if (e instanceof F.Component) {
    var n;
    return (n = at.findDOMNode) === null || n === void 0 ? void 0 : n.call(at, e);
  }
  return null;
}
var $t = {
  exports: {}
}, g = {};
/**
 * @license React
 * react-is.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ge = Symbol.for("react.element"), qe = Symbol.for("react.portal"), me = Symbol.for("react.fragment"), ye = Symbol.for("react.strict_mode"), Ee = Symbol.for("react.profiler"), ge = Symbol.for("react.provider"), he = Symbol.for("react.context"), br = Symbol.for("react.server_context"), be = Symbol.for("react.forward_ref"), _e = Symbol.for("react.suspense"), Se = Symbol.for("react.suspense_list"), we = Symbol.for("react.memo"), Ce = Symbol.for("react.lazy"), _r = Symbol.for("react.offscreen"), Dt;
Dt = Symbol.for("react.module.reference");
function I(e) {
  if (typeof e == "object" && e !== null) {
    var t = e.$$typeof;
    switch (t) {
      case Ge:
        switch (e = e.type, e) {
          case me:
          case Ee:
          case ye:
          case _e:
          case Se:
            return e;
          default:
            switch (e = e && e.$$typeof, e) {
              case br:
              case he:
              case be:
              case Ce:
              case we:
              case ge:
                return e;
              default:
                return t;
            }
        }
      case qe:
        return t;
    }
  }
}
g.ContextConsumer = he;
g.ContextProvider = ge;
g.Element = Ge;
g.ForwardRef = be;
g.Fragment = me;
g.Lazy = Ce;
g.Memo = we;
g.Portal = qe;
g.Profiler = Ee;
g.StrictMode = ye;
g.Suspense = _e;
g.SuspenseList = Se;
g.isAsyncMode = function() {
  return !1;
};
g.isConcurrentMode = function() {
  return !1;
};
g.isContextConsumer = function(e) {
  return I(e) === he;
};
g.isContextProvider = function(e) {
  return I(e) === ge;
};
g.isElement = function(e) {
  return typeof e == "object" && e !== null && e.$$typeof === Ge;
};
g.isForwardRef = function(e) {
  return I(e) === be;
};
g.isFragment = function(e) {
  return I(e) === me;
};
g.isLazy = function(e) {
  return I(e) === Ce;
};
g.isMemo = function(e) {
  return I(e) === we;
};
g.isPortal = function(e) {
  return I(e) === qe;
};
g.isProfiler = function(e) {
  return I(e) === Ee;
};
g.isStrictMode = function(e) {
  return I(e) === ye;
};
g.isSuspense = function(e) {
  return I(e) === _e;
};
g.isSuspenseList = function(e) {
  return I(e) === Se;
};
g.isValidElementType = function(e) {
  return typeof e == "string" || typeof e == "function" || e === me || e === Ee || e === ye || e === _e || e === Se || e === _r || typeof e == "object" && e !== null && (e.$$typeof === Ce || e.$$typeof === we || e.$$typeof === ge || e.$$typeof === he || e.$$typeof === be || e.$$typeof === Dt || e.getModuleId !== void 0);
};
g.typeOf = I;
$t.exports = g;
var ke = $t.exports, Sr = Symbol.for("react.element"), wr = Symbol.for("react.transitional.element"), Cr = Symbol.for("react.fragment");
function Rr(e) {
  return (
    // Base object type
    e && k(e) === "object" && // React Element type
    (e.$$typeof === Sr || e.$$typeof === wr) && // React Fragment type
    e.type === Cr
  );
}
var Pr = function(t, n) {
  typeof t == "function" ? t(n) : k(t) === "object" && t && "current" in t && (t.current = n);
}, xr = function(t) {
  var n, r;
  if (!t)
    return !1;
  if (Ft(t) && t.props.propertyIsEnumerable("ref"))
    return !0;
  var o = ke.isMemo(t) ? t.type.type : t.type;
  return !(typeof o == "function" && !((n = o.prototype) !== null && n !== void 0 && n.render) && o.$$typeof !== ke.ForwardRef || typeof t == "function" && !((r = t.prototype) !== null && r !== void 0 && r.render) && t.$$typeof !== ke.ForwardRef);
};
function Ft(e) {
  return /* @__PURE__ */ mn(e) && !Rr(e);
}
var Tr = function(t) {
  if (t && Ft(t)) {
    var n = t;
    return n.props.propertyIsEnumerable("ref") ? n.props.ref : n.ref;
  }
  return null;
};
function Ar(e, t) {
  if (e == null) return {};
  var n = {};
  for (var r in e) if ({}.hasOwnProperty.call(e, r)) {
    if (t.includes(r)) continue;
    n[r] = e[r];
  }
  return n;
}
function bt(e, t) {
  if (e == null) return {};
  var n, r, o = Ar(e, t);
  if (Object.getOwnPropertySymbols) {
    var i = Object.getOwnPropertySymbols(e);
    for (r = 0; r < i.length; r++) n = i[r], t.includes(n) || {}.propertyIsEnumerable.call(e, n) && (o[n] = e[n]);
  }
  return o;
}
var Or = /* @__PURE__ */ v.createContext({});
function Ut(e, t) {
  if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function _t(e, t) {
  for (var n = 0; n < t.length; n++) {
    var r = t[n];
    r.enumerable = r.enumerable || !1, r.configurable = !0, "value" in r && (r.writable = !0), Object.defineProperty(e, Mt(r.key), r);
  }
}
function Vt(e, t, n) {
  return t && _t(e.prototype, t), n && _t(e, n), Object.defineProperty(e, "prototype", {
    writable: !1
  }), e;
}
function De(e, t) {
  return De = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function(n, r) {
    return n.__proto__ = r, n;
  }, De(e, t);
}
function Kt(e, t) {
  if (typeof t != "function" && t !== null) throw new TypeError("Super expression must either be null or a function");
  e.prototype = Object.create(t && t.prototype, {
    constructor: {
      value: e,
      writable: !0,
      configurable: !0
    }
  }), Object.defineProperty(e, "prototype", {
    writable: !1
  }), t && De(e, t);
}
function pe(e) {
  return pe = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function(t) {
    return t.__proto__ || Object.getPrototypeOf(t);
  }, pe(e);
}
function Wt() {
  try {
    var e = !Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function() {
    }));
  } catch {
  }
  return (Wt = function() {
    return !!e;
  })();
}
function Fe(e) {
  if (e === void 0) throw new ReferenceError("this hasn't been initialised - super() hasn't been called");
  return e;
}
function Lr(e, t) {
  if (t && (k(t) == "object" || typeof t == "function")) return t;
  if (t !== void 0) throw new TypeError("Derived constructors may only return object or undefined");
  return Fe(e);
}
function Ht(e) {
  var t = Wt();
  return function() {
    var n, r = pe(e);
    if (t) {
      var o = pe(this).constructor;
      n = Reflect.construct(r, arguments, o);
    } else n = r.apply(this, arguments);
    return Lr(this, n);
  };
}
var kr = /* @__PURE__ */ function(e) {
  Kt(n, e);
  var t = Ht(n);
  function n() {
    return Ut(this, n), t.apply(this, arguments);
  }
  return Vt(n, [{
    key: "render",
    value: function() {
      return this.props.children;
    }
  }]), n;
}(v.Component);
function Ue(e) {
  var t = v.useRef();
  t.current = e;
  var n = v.useCallback(function() {
    for (var r, o = arguments.length, i = new Array(o), a = 0; a < o; a++)
      i[a] = arguments[a];
    return (r = t.current) === null || r === void 0 ? void 0 : r.call.apply(r, [t].concat(i));
  }, []);
  return n;
}
function Ye() {
  return !!(typeof window < "u" && window.document && window.document.createElement);
}
function Ve(e) {
  var t = v.useRef(!1), n = v.useState(e), r = D(n, 2), o = r[0], i = r[1];
  v.useEffect(function() {
    return t.current = !1, function() {
      t.current = !0;
    };
  }, []);
  function a(s, l) {
    l && t.current || i(s);
  }
  return [o, a];
}
function Ir(e) {
  var t = v.useReducer(function(s) {
    return s + 1;
  }, 0), n = D(t, 2), r = n[1], o = v.useRef(e), i = Ue(function() {
    return o.current;
  }), a = Ue(function(s) {
    o.current = typeof s == "function" ? s(o.current) : s, r();
  });
  return [i, a];
}
var V = "none", ie = "appear", ae = "enter", se = "leave", St = "none", N = "prepare", J = "start", X = "active", Je = "end", zt = "prepared";
function wt(e, t) {
  var n = {};
  return n[e.toLowerCase()] = t.toLowerCase(), n["Webkit".concat(e)] = "webkit".concat(t), n["Moz".concat(e)] = "moz".concat(t), n["ms".concat(e)] = "MS".concat(t), n["O".concat(e)] = "o".concat(t.toLowerCase()), n;
}
function jr(e, t) {
  var n = {
    animationend: wt("Animation", "AnimationEnd"),
    transitionend: wt("Transition", "TransitionEnd")
  };
  return e && ("AnimationEvent" in t || delete n.animationend.animation, "TransitionEvent" in t || delete n.transitionend.transition), n;
}
var Nr = jr(Ye(), typeof window < "u" ? window : {}), Bt = {};
if (Ye()) {
  var Mr = document.createElement("div");
  Bt = Mr.style;
}
var ue = {};
function Qt(e) {
  if (ue[e])
    return ue[e];
  var t = Nr[e];
  if (t)
    for (var n = Object.keys(t), r = n.length, o = 0; o < r; o += 1) {
      var i = n[o];
      if (Object.prototype.hasOwnProperty.call(t, i) && i in Bt)
        return ue[e] = t[i], ue[e];
    }
  return "";
}
var Gt = Qt("animationend"), qt = Qt("transitionend"), Yt = !!(Gt && qt), Ct = Gt || "animationend", Rt = qt || "transitionend";
function Pt(e, t) {
  if (!e) return null;
  if (k(e) === "object") {
    var n = t.replace(/-\w/g, function(r) {
      return r[1].toUpperCase();
    });
    return e[n];
  }
  return "".concat(e, "-").concat(t);
}
const $r = function(e) {
  var t = K();
  function n(o) {
    o && (o.removeEventListener(Rt, e), o.removeEventListener(Ct, e));
  }
  function r(o) {
    t.current && t.current !== o && n(t.current), o && o !== t.current && (o.addEventListener(Rt, e), o.addEventListener(Ct, e), t.current = o);
  }
  return v.useEffect(function() {
    return function() {
      n(t.current);
    };
  }, []), [r, n];
};
var Jt = Ye() ? yn : ee, Xt = function(t) {
  return +setTimeout(t, 16);
}, Zt = function(t) {
  return clearTimeout(t);
};
typeof window < "u" && "requestAnimationFrame" in window && (Xt = function(t) {
  return window.requestAnimationFrame(t);
}, Zt = function(t) {
  return window.cancelAnimationFrame(t);
});
var xt = 0, Xe = /* @__PURE__ */ new Map();
function en(e) {
  Xe.delete(e);
}
var Ke = function(t) {
  var n = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 1;
  xt += 1;
  var r = xt;
  function o(i) {
    if (i === 0)
      en(r), t();
    else {
      var a = Xt(function() {
        o(i - 1);
      });
      Xe.set(r, a);
    }
  }
  return o(n), r;
};
Ke.cancel = function(e) {
  var t = Xe.get(e);
  return en(e), Zt(t);
};
const Dr = function() {
  var e = v.useRef(null);
  function t() {
    Ke.cancel(e.current);
  }
  function n(r) {
    var o = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : 2;
    t();
    var i = Ke(function() {
      o <= 1 ? r({
        isCanceled: function() {
          return i !== e.current;
        }
      }) : n(r, o - 1);
    });
    e.current = i;
  }
  return v.useEffect(function() {
    return function() {
      t();
    };
  }, []), [n, t];
};
var Fr = [N, J, X, Je], Ur = [N, zt], tn = !1, Vr = !0;
function nn(e) {
  return e === X || e === Je;
}
const Kr = function(e, t, n) {
  var r = Ve(St), o = D(r, 2), i = o[0], a = o[1], s = Dr(), l = D(s, 2), c = l[0], p = l[1];
  function u() {
    a(N, !0);
  }
  var d = t ? Ur : Fr;
  return Jt(function() {
    if (i !== St && i !== Je) {
      var f = d.indexOf(i), _ = d[f + 1], y = n(i);
      y === tn ? a(_, !0) : _ && c(function(h) {
        function S() {
          h.isCanceled() || a(_, !0);
        }
        y === !0 ? S() : Promise.resolve(y).then(S);
      });
    }
  }, [e, i]), v.useEffect(function() {
    return function() {
      p();
    };
  }, []), [u, i];
};
function Wr(e, t, n, r) {
  var o = r.motionEnter, i = o === void 0 ? !0 : o, a = r.motionAppear, s = a === void 0 ? !0 : a, l = r.motionLeave, c = l === void 0 ? !0 : l, p = r.motionDeadline, u = r.motionLeaveImmediately, d = r.onAppearPrepare, f = r.onEnterPrepare, _ = r.onLeavePrepare, y = r.onAppearStart, h = r.onEnterStart, S = r.onLeaveStart, P = r.onAppearActive, w = r.onEnterActive, E = r.onLeaveActive, x = r.onAppearEnd, m = r.onEnterEnd, C = r.onLeaveEnd, L = r.onVisibleChanged, Q = Ve(), G = D(Q, 2), j = G[0], W = G[1], A = Ir(V), H = D(A, 2), U = H[0], z = H[1], Re = Ve(null), q = D(Re, 2), an = q[0], Ze = q[1], M = U(), te = K(!1), Pe = K(null);
  function ne() {
    return n();
  }
  var et = K(!1);
  function tt() {
    z(V), Ze(null, !0);
  }
  var nt = Ue(function(O) {
    var R = U();
    if (R !== V) {
      var $ = ne();
      if (!(O && !O.deadline && O.target !== $)) {
        var re = et.current, oe;
        R === ie && re ? oe = x == null ? void 0 : x($, O) : R === ae && re ? oe = m == null ? void 0 : m($, O) : R === se && re && (oe = C == null ? void 0 : C($, O)), re && oe !== !1 && tt();
      }
    }
  }), sn = $r(nt), un = D(sn, 1), cn = un[0], rt = function(R) {
    switch (R) {
      case ie:
        return T(T(T({}, N, d), J, y), X, P);
      case ae:
        return T(T(T({}, N, f), J, h), X, w);
      case se:
        return T(T(T({}, N, _), J, S), X, E);
      default:
        return {};
    }
  }, Z = v.useMemo(function() {
    return rt(M);
  }, [M]), ln = Kr(M, !e, function(O) {
    if (O === N) {
      var R = Z[N];
      return R ? R(ne()) : tn;
    }
    if (B in Z) {
      var $;
      Ze((($ = Z[B]) === null || $ === void 0 ? void 0 : $.call(Z, ne(), null)) || null);
    }
    return B === X && M !== V && (cn(ne()), p > 0 && (clearTimeout(Pe.current), Pe.current = setTimeout(function() {
      nt({
        deadline: !0
      });
    }, p))), B === zt && tt(), Vr;
  }), ot = D(ln, 2), fn = ot[0], B = ot[1], dn = nn(B);
  et.current = dn;
  var it = K(null);
  Jt(function() {
    if (!(te.current && it.current === t)) {
      W(t);
      var O = te.current;
      te.current = !0;
      var R;
      !O && t && s && (R = ie), O && t && i && (R = ae), (O && !t && c || !O && u && !t && c) && (R = se);
      var $ = rt(R);
      R && (e || $[N]) ? (z(R), fn()) : z(V), it.current = t;
    }
  }, [t]), ee(function() {
    // Cancel appear
    (M === ie && !s || // Cancel enter
    M === ae && !i || // Cancel leave
    M === se && !c) && z(V);
  }, [s, i, c]), ee(function() {
    return function() {
      te.current = !1, clearTimeout(Pe.current);
    };
  }, []);
  var xe = v.useRef(!1);
  ee(function() {
    j && (xe.current = !0), j !== void 0 && M === V && ((xe.current || j) && (L == null || L(j)), xe.current = !0);
  }, [j, M]);
  var Te = an;
  return Z[N] && B === J && (Te = b({
    transition: "none"
  }, Te)), [M, B, Te, j ?? t];
}
function Hr(e) {
  var t = e;
  k(e) === "object" && (t = e.transitionSupport);
  function n(o, i) {
    return !!(o.motionName && t && i !== !1);
  }
  var r = /* @__PURE__ */ v.forwardRef(function(o, i) {
    var a = o.visible, s = a === void 0 ? !0 : a, l = o.removeOnLeave, c = l === void 0 ? !0 : l, p = o.forceRender, u = o.children, d = o.motionName, f = o.leavedClassName, _ = o.eventProps, y = v.useContext(Or), h = y.motion, S = n(o, h), P = K(), w = K();
    function E() {
      try {
        return P.current instanceof HTMLElement ? P.current : hr(w.current);
      } catch {
        return null;
      }
    }
    var x = Wr(S, s, E, o), m = D(x, 4), C = m[0], L = m[1], Q = m[2], G = m[3], j = v.useRef(G);
    G && (j.current = !0);
    var W = v.useCallback(function(q) {
      P.current = q, Pr(i, q);
    }, [i]), A, H = b(b({}, _), {}, {
      visible: s
    });
    if (!u)
      A = null;
    else if (C === V)
      G ? A = u(b({}, H), W) : !c && j.current && f ? A = u(b(b({}, H), {}, {
        className: f
      }), W) : p || !c && !f ? A = u(b(b({}, H), {}, {
        style: {
          display: "none"
        }
      }), W) : A = null;
    else {
      var U;
      L === N ? U = "prepare" : nn(L) ? U = "active" : L === J && (U = "start");
      var z = Pt(d, "".concat(C, "-").concat(U));
      A = u(b(b({}, H), {}, {
        className: le(Pt(d, C), T(T({}, z, z && U), d, typeof d == "string")),
        style: Q
      }), W);
    }
    if (/* @__PURE__ */ v.isValidElement(A) && xr(A)) {
      var Re = Tr(A);
      Re || (A = /* @__PURE__ */ v.cloneElement(A, {
        ref: W
      }));
    }
    return /* @__PURE__ */ v.createElement(kr, {
      ref: w
    }, A);
  });
  return r.displayName = "CSSMotion", r;
}
const rn = Hr(Yt);
function We() {
  return We = Object.assign ? Object.assign.bind() : function(e) {
    for (var t = 1; t < arguments.length; t++) {
      var n = arguments[t];
      for (var r in n) ({}).hasOwnProperty.call(n, r) && (e[r] = n[r]);
    }
    return e;
  }, We.apply(null, arguments);
}
var He = "add", ze = "keep", Be = "remove", Ie = "removed";
function zr(e) {
  var t;
  return e && k(e) === "object" && "key" in e ? t = e : t = {
    key: e
  }, b(b({}, t), {}, {
    key: String(t.key)
  });
}
function Qe() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [];
  return e.map(zr);
}
function Br() {
  var e = arguments.length > 0 && arguments[0] !== void 0 ? arguments[0] : [], t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : [], n = [], r = 0, o = t.length, i = Qe(e), a = Qe(t);
  i.forEach(function(c) {
    for (var p = !1, u = r; u < o; u += 1) {
      var d = a[u];
      if (d.key === c.key) {
        r < u && (n = n.concat(a.slice(r, u).map(function(f) {
          return b(b({}, f), {}, {
            status: He
          });
        })), r = u), n.push(b(b({}, d), {}, {
          status: ze
        })), r += 1, p = !0;
        break;
      }
    }
    p || n.push(b(b({}, c), {}, {
      status: Be
    }));
  }), r < o && (n = n.concat(a.slice(r).map(function(c) {
    return b(b({}, c), {}, {
      status: He
    });
  })));
  var s = {};
  n.forEach(function(c) {
    var p = c.key;
    s[p] = (s[p] || 0) + 1;
  });
  var l = Object.keys(s).filter(function(c) {
    return s[c] > 1;
  });
  return l.forEach(function(c) {
    n = n.filter(function(p) {
      var u = p.key, d = p.status;
      return u !== c || d !== Be;
    }), n.forEach(function(p) {
      p.key === c && (p.status = ze);
    });
  }), n;
}
var Qr = ["component", "children", "onVisibleChanged", "onAllRemoved"], Gr = ["status"], qr = ["eventProps", "visible", "children", "motionName", "motionAppear", "motionEnter", "motionLeave", "motionLeaveImmediately", "motionDeadline", "removeOnLeave", "leavedClassName", "onAppearPrepare", "onAppearStart", "onAppearActive", "onAppearEnd", "onEnterStart", "onEnterActive", "onEnterEnd", "onLeaveStart", "onLeaveActive", "onLeaveEnd"];
function Yr(e) {
  var t = arguments.length > 1 && arguments[1] !== void 0 ? arguments[1] : rn, n = /* @__PURE__ */ function(r) {
    Kt(i, r);
    var o = Ht(i);
    function i() {
      var a;
      Ut(this, i);
      for (var s = arguments.length, l = new Array(s), c = 0; c < s; c++)
        l[c] = arguments[c];
      return a = o.call.apply(o, [this].concat(l)), T(Fe(a), "state", {
        keyEntities: []
      }), T(Fe(a), "removeKey", function(p) {
        a.setState(function(u) {
          var d = u.keyEntities.map(function(f) {
            return f.key !== p ? f : b(b({}, f), {}, {
              status: Ie
            });
          });
          return {
            keyEntities: d
          };
        }, function() {
          var u = a.state.keyEntities, d = u.filter(function(f) {
            var _ = f.status;
            return _ !== Ie;
          }).length;
          d === 0 && a.props.onAllRemoved && a.props.onAllRemoved();
        });
      }), a;
    }
    return Vt(i, [{
      key: "render",
      value: function() {
        var s = this, l = this.state.keyEntities, c = this.props, p = c.component, u = c.children, d = c.onVisibleChanged;
        c.onAllRemoved;
        var f = bt(c, Qr), _ = p || v.Fragment, y = {};
        return qr.forEach(function(h) {
          y[h] = f[h], delete f[h];
        }), delete f.keys, /* @__PURE__ */ v.createElement(_, f, l.map(function(h, S) {
          var P = h.status, w = bt(h, Gr), E = P === He || P === ze;
          return /* @__PURE__ */ v.createElement(t, We({}, y, {
            key: w.key,
            visible: E,
            eventProps: w,
            onVisibleChanged: function(m) {
              d == null || d(m, {
                key: w.key
              }), m || s.removeKey(w.key);
            }
          }), function(x, m) {
            return u(b(b({}, x), {}, {
              index: S
            }), m);
          });
        }));
      }
    }], [{
      key: "getDerivedStateFromProps",
      value: function(s, l) {
        var c = s.keys, p = l.keyEntities, u = Qe(c), d = Br(p, u);
        return {
          keyEntities: d.filter(function(f) {
            var _ = p.find(function(y) {
              var h = y.key;
              return f.key === h;
            });
            return !(_ && _.status === Ie && f.status === Be);
          })
        };
      }
    }]), i;
  }(v.Component);
  return T(n, "defaultProps", {
    component: "div"
  }), n;
}
Yr(Yt);
const on = /* @__PURE__ */ v.createContext({}), Tt = () => ({
  height: 0
}), At = (e) => ({
  height: e.scrollHeight
});
function Jr(e) {
  const {
    title: t,
    onOpenChange: n,
    open: r,
    children: o,
    className: i,
    style: a,
    classNames: s = {},
    styles: l = {},
    closable: c,
    forceRender: p
  } = e, {
    prefixCls: u
  } = v.useContext(on), d = `${u}-header`;
  return /* @__PURE__ */ v.createElement(rn, {
    motionEnter: !0,
    motionLeave: !0,
    motionName: `${d}-motion`,
    leavedClassName: `${d}-motion-hidden`,
    onEnterStart: Tt,
    onEnterActive: At,
    onLeaveStart: At,
    onLeaveActive: Tt,
    visible: r,
    forceRender: p
  }, ({
    className: f,
    style: _
  }) => /* @__PURE__ */ v.createElement("div", {
    className: le(d, f, i),
    style: {
      ..._,
      ...a
    }
  }, (c !== !1 || t) && /* @__PURE__ */ v.createElement("div", {
    className: (
      // We follow antd naming standard here.
      // So the header part is use `-header` suffix.
      // Though its little bit weird for double `-header`.
      le(`${d}-header`, s.header)
    ),
    style: {
      ...l.header
    }
  }, /* @__PURE__ */ v.createElement("div", {
    className: `${d}-title`
  }, t), c !== !1 && /* @__PURE__ */ v.createElement("div", {
    className: `${d}-close`
  }, /* @__PURE__ */ v.createElement(Sn, {
    type: "text",
    icon: /* @__PURE__ */ v.createElement(_n, null),
    size: "small",
    onClick: () => {
      n == null || n(!r);
    }
  }))), o && /* @__PURE__ */ v.createElement("div", {
    className: le(`${d}-content`, s.content),
    style: {
      ...l.content
    }
  }, o)));
}
const Zr = sr(({
  slots: e,
  ...t
}) => {
  const {
    getPrefixCls: n
  } = F.useContext(wn.ConfigContext);
  return /* @__PURE__ */ Oe.jsx(on.Provider, {
    value: {
      prefixCls: n("sender")
    },
    children: /* @__PURE__ */ Oe.jsx(Jr, {
      ...t,
      title: e.title ? /* @__PURE__ */ Oe.jsx(dr, {
        slot: e.title
      }) : t.title
    })
  });
});
export {
  Zr as SenderHeader,
  Zr as default
};
