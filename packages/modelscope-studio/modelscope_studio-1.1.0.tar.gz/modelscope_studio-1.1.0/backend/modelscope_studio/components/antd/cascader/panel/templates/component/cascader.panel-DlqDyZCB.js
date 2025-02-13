import { i as ae, a as M, r as ue, b as de, g as fe, w as k } from "./Index-CfMtFh80.js";
const y = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, A = window.ms_globals.React.useRef, $ = window.ms_globals.React.useState, F = window.ms_globals.React.useEffect, ce = window.ms_globals.React.useMemo, W = window.ms_globals.ReactDOM.createPortal, me = window.ms_globals.internalContext.useContextPropsContext, B = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.Cascader, he = window.ms_globals.createItemsContext.createItemsContext;
var pe = /\s/;
function ge(t) {
  for (var e = t.length; e-- && pe.test(t.charAt(e)); )
    ;
  return e;
}
var be = /^\s+/;
function xe(t) {
  return t && t.slice(0, ge(t) + 1).replace(be, "");
}
var H = NaN, we = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ye = parseInt;
function q(t) {
  if (typeof t == "number")
    return t;
  if (ae(t))
    return H;
  if (M(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = M(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = xe(t);
  var s = Ce.test(t);
  return s || Ee.test(t) ? ye(t.slice(2), s ? 2 : 8) : we.test(t) ? H : +t;
}
var L = function() {
  return ue.Date.now();
}, Ie = "Expected a function", ve = Math.max, Re = Math.min;
function Se(t, e, s) {
  var l, o, n, r, i, a, m = 0, _ = !1, c = !1, g = !0;
  if (typeof t != "function")
    throw new TypeError(Ie);
  e = q(e) || 0, M(s) && (_ = !!s.leading, c = "maxWait" in s, n = c ? ve(q(s.maxWait) || 0, e) : n, g = "trailing" in s ? !!s.trailing : g);
  function d(p) {
    var E = l, S = o;
    return l = o = void 0, m = p, r = t.apply(S, E), r;
  }
  function x(p) {
    return m = p, i = setTimeout(b, e), _ ? d(p) : r;
  }
  function f(p) {
    var E = p - a, S = p - m, U = e - E;
    return c ? Re(U, n - S) : U;
  }
  function h(p) {
    var E = p - a, S = p - m;
    return a === void 0 || E >= e || E < 0 || c && S >= n;
  }
  function b() {
    var p = L();
    if (h(p))
      return C(p);
    i = setTimeout(b, f(p));
  }
  function C(p) {
    return i = void 0, g && l ? d(p) : (l = o = void 0, r);
  }
  function I() {
    i !== void 0 && clearTimeout(i), m = 0, l = a = o = i = void 0;
  }
  function u() {
    return i === void 0 ? r : C(L());
  }
  function v() {
    var p = L(), E = h(p);
    if (l = arguments, o = this, a = p, E) {
      if (i === void 0)
        return x(a);
      if (c)
        return clearTimeout(i), i = setTimeout(b, e), d(a);
    }
    return i === void 0 && (i = setTimeout(b, e)), r;
  }
  return v.cancel = I, v.flush = u, v;
}
function ke(t, e) {
  return de(t, e);
}
var ee = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Oe = y, Pe = Symbol.for("react.element"), Te = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Oe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(t, e, s) {
  var l, o = {}, n = null, r = null;
  s !== void 0 && (n = "" + s), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (l in e) je.call(e, l) && !Ne.hasOwnProperty(l) && (o[l] = e[l]);
  if (t && t.defaultProps) for (l in e = t.defaultProps, e) o[l] === void 0 && (o[l] = e[l]);
  return {
    $$typeof: Pe,
    type: t,
    key: n,
    ref: r,
    props: o,
    _owner: Le.current
  };
}
j.Fragment = Te;
j.jsx = te;
j.jsxs = te;
ee.exports = j;
var w = ee.exports;
const {
  SvelteComponent: Ae,
  assign: z,
  binding_callbacks: G,
  check_outros: Fe,
  children: ne,
  claim_element: re,
  claim_space: We,
  component_subscribe: J,
  compute_slots: Me,
  create_slot: De,
  detach: R,
  element: oe,
  empty: X,
  exclude_internal_props: Y,
  get_all_dirty_from_scope: Ve,
  get_slot_changes: Ue,
  group_outros: Be,
  init: He,
  insert_hydration: O,
  safe_not_equal: qe,
  set_custom_element_data: se,
  space: ze,
  transition_in: P,
  transition_out: D,
  update_slot_base: Ge
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Ke
} = window.__gradio__svelte__internal;
function K(t) {
  let e, s;
  const l = (
    /*#slots*/
    t[7].default
  ), o = De(
    l,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = oe("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      e = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(e);
      o && o.l(r), r.forEach(R), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, e, r), o && o.m(e, null), t[9](e), s = !0;
    },
    p(n, r) {
      o && o.p && (!s || r & /*$$scope*/
      64) && Ge(
        o,
        l,
        n,
        /*$$scope*/
        n[6],
        s ? Ue(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ve(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      s || (P(o, n), s = !0);
    },
    o(n) {
      D(o, n), s = !1;
    },
    d(n) {
      n && R(e), o && o.d(n), t[9](null);
    }
  };
}
function Qe(t) {
  let e, s, l, o, n = (
    /*$$slots*/
    t[4].default && K(t)
  );
  return {
    c() {
      e = oe("react-portal-target"), s = ze(), n && n.c(), l = X(), this.h();
    },
    l(r) {
      e = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(e).forEach(R), s = We(r), n && n.l(r), l = X(), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, s, i), n && n.m(r, i), O(r, l, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = K(r), n.c(), P(n, 1), n.m(l.parentNode, l)) : n && (Be(), D(n, 1, 1, () => {
        n = null;
      }), Fe());
    },
    i(r) {
      o || (P(n), o = !0);
    },
    o(r) {
      D(n), o = !1;
    },
    d(r) {
      r && (R(e), R(s), R(l)), t[8](null), n && n.d(r);
    }
  };
}
function Q(t) {
  const {
    svelteInit: e,
    ...s
  } = t;
  return s;
}
function Ze(t, e, s) {
  let l, o, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = Me(n);
  let {
    svelteInit: a
  } = e;
  const m = k(Q(e)), _ = k();
  J(t, _, (u) => s(0, l = u));
  const c = k();
  J(t, c, (u) => s(1, o = u));
  const g = [], d = Xe("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h
  } = fe() || {}, b = a({
    parent: d,
    props: m,
    target: _,
    slot: c,
    slotKey: x,
    slotIndex: f,
    subSlotIndex: h,
    onDestroy(u) {
      g.push(u);
    }
  });
  Ke("$$ms-gr-react-wrapper", b), Je(() => {
    m.set(Q(e));
  }), Ye(() => {
    g.forEach((u) => u());
  });
  function C(u) {
    G[u ? "unshift" : "push"](() => {
      l = u, _.set(l);
    });
  }
  function I(u) {
    G[u ? "unshift" : "push"](() => {
      o = u, c.set(o);
    });
  }
  return t.$$set = (u) => {
    s(17, e = z(z({}, e), Y(u))), "svelteInit" in u && s(5, a = u.svelteInit), "$$scope" in u && s(6, r = u.$$scope);
  }, e = Y(e), [l, o, _, c, i, a, r, n, C, I];
}
class $e extends Ae {
  constructor(e) {
    super(), He(this, e, Ze, Qe, qe, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, N = window.ms_globals.tree;
function et(t, e = {}) {
  function s(l) {
    const o = k(), n = new $e({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], Z({
            createPortal: W,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((m) => m.svelteInstance !== o), Z({
              createPortal: W,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(s);
    });
  });
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(t) {
  return t ? Object.keys(t).reduce((e, s) => {
    const l = t[s];
    return e[s] = rt(s, l), e;
  }, {}) : {};
}
function rt(t, e) {
  return typeof e == "number" && !tt.includes(t) ? e + "px" : e;
}
function V(t) {
  const e = [], s = t.cloneNode(!1);
  if (t._reactElement) {
    const o = y.Children.toArray(t._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = V(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = t._reactElement.props.children, e.push(W(y.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: o
    }), s)), {
      clonedElement: s,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      s.addEventListener(i, r, a);
    });
  });
  const l = Array.from(t.childNodes);
  for (let o = 0; o < l.length; o++) {
    const n = l[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = V(n);
      e.push(...i), s.appendChild(r);
    } else n.nodeType === 3 && s.appendChild(n.cloneNode());
  }
  return {
    clonedElement: s,
    portals: e
  };
}
function ot(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const T = ie(({
  slot: t,
  clone: e,
  className: s,
  style: l,
  observeAttributes: o
}, n) => {
  const r = A(), [i, a] = $([]), {
    forceClone: m
  } = me(), _ = m ? !0 : e;
  return F(() => {
    var x;
    if (!r.current || !t)
      return;
    let c = t;
    function g() {
      let f = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (f = c.children[0], f.tagName.toLowerCase() === "react-portal-target" && f.children[0] && (f = f.children[0])), ot(n, f), s && f.classList.add(...s.split(" ")), l) {
        const h = nt(l);
        Object.keys(h).forEach((b) => {
          f.style[b] = h[b];
        });
      }
    }
    let d = null;
    if (_ && window.MutationObserver) {
      let f = function() {
        var I, u, v;
        (I = r.current) != null && I.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: b,
          clonedElement: C
        } = V(t);
        c = C, a(b), c.style.display = "contents", g(), (v = r.current) == null || v.appendChild(c);
      };
      f();
      const h = Se(() => {
        f(), d == null || d.disconnect(), d == null || d.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      d = new window.MutationObserver(h), d.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var f, h;
      c.style.display = "", (f = r.current) != null && f.contains(c) && ((h = r.current) == null || h.removeChild(c)), d == null || d.disconnect();
    };
  }, [t, _, s, l, n, o]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function st({
  value: t,
  onValueChange: e
}) {
  const [s, l] = $(t), o = A(e);
  o.current = e;
  const n = A(s);
  return n.current = s, F(() => {
    o.current(s);
  }, [s]), F(() => {
    ke(t, n.current) || l(t);
  }, [t]), [s, l];
}
function le(t, e, s) {
  const l = t.filter(Boolean);
  if (l.length !== 0)
    return l.map((o, n) => {
      var m;
      if (typeof o != "object")
        return e != null && e.fallback ? e.fallback(o) : o;
      const r = {
        ...o.props,
        key: ((m = o.props) == null ? void 0 : m.key) ?? (s ? `${s}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((_) => {
        if (!o.slots[_] || !(o.slots[_] instanceof Element) && !o.slots[_].el)
          return;
        const c = _.split(".");
        c.forEach((b, C) => {
          i[b] || (i[b] = {}), C !== c.length - 1 && (i = r[b]);
        });
        const g = o.slots[_];
        let d, x, f = (e == null ? void 0 : e.clone) ?? !1, h = e == null ? void 0 : e.forceClone;
        g instanceof Element ? d = g : (d = g.el, x = g.callback, f = g.clone ?? f, h = g.forceClone ?? h), h = h ?? !!x, i[c[c.length - 1]] = d ? x ? (...b) => (x(c[c.length - 1], b), /* @__PURE__ */ w.jsx(B, {
          params: b,
          forceClone: h,
          children: /* @__PURE__ */ w.jsx(T, {
            slot: d,
            clone: f
          })
        })) : /* @__PURE__ */ w.jsx(B, {
          forceClone: h,
          children: /* @__PURE__ */ w.jsx(T, {
            slot: d,
            clone: f
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return o[a] ? r[a] = le(o[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
const {
  useItems: lt,
  withItemsContextProvider: it,
  ItemHandler: at
} = he("antd-cascader-options"), ut = et(it(["default", "options"], ({
  slots: t,
  children: e,
  onValueChange: s,
  onChange: l,
  onLoadData: o,
  options: n,
  ...r
}) => {
  const [i, a] = st({
    onValueChange: s,
    value: r.value
  }), {
    items: m
  } = lt(), _ = m.options.length > 0 ? m.options : m.default;
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [/* @__PURE__ */ w.jsx("div", {
      style: {
        display: "none"
      },
      children: e
    }), /* @__PURE__ */ w.jsx(_e.Panel, {
      ...r,
      value: i,
      options: ce(() => n || le(_, {
        clone: !0
      }), [n, _]),
      loadData: o,
      onChange: (c, ...g) => {
        l == null || l(c, ...g), a(c);
      },
      expandIcon: t.expandIcon ? /* @__PURE__ */ w.jsx(T, {
        slot: t.expandIcon
      }) : r.expandIcon,
      notFoundContent: t.notFoundContent ? /* @__PURE__ */ w.jsx(T, {
        slot: t.notFoundContent
      }) : r.notFoundContent
    })]
  });
}));
export {
  ut as CascaderPanel,
  ut as default
};
